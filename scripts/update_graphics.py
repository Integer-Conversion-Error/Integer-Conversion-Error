"""Refresh profile SVGs, preserving existing images when a service fails."""

import json
import math
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timedelta
from html import escape
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo


ASSETS = Path(__file__).resolve().parents[1] / "assets"
USERNAME = os.environ.get("PROFILE_USERNAME", "Integer-Conversion-Error")


def save_svg(filename, content):
    content = ("\n".join(line.rstrip() for line in content.decode().splitlines()).strip() + "\n").encode()
    root = ET.fromstring(content)
    if root.tag != "{http://www.w3.org/2000/svg}svg":
        raise ValueError("Response is not an SVG")
    path = ASSETS / filename
    temporary = path.with_suffix(".tmp")
    temporary.write_bytes(content)
    temporary.replace(path)


def download_card(filename, endpoint, options, expected_text):
    url = endpoint + "?" + urlencode(options)
    request = Request(url, headers={"User-Agent": "github-profile-graphics"})
    with urlopen(request, timeout=45) as response:
        content = response.read()
    root = ET.fromstring(content)
    # Some card services return error messages inside a valid SVG with HTTP 200.
    text = " ".join(root.itertext())
    if expected_text not in text:
        raise ValueError("Response does not contain the expected statistics")
    save_svg(filename, content)


def activity_graph():
    today = datetime.now(ZoneInfo("America/Toronto")).date()
    start = today - timedelta(days=30)
    query = """
      query($login: String!, $from: DateTime!, $to: DateTime!) {
        user(login: $login) {
          contributionsCollection(from: $from, to: $to) {
            contributionCalendar {
              weeks { contributionDays { date contributionCount } }
            }
          }
        }
      }
    """
    # gh reads GH_TOKEN in Actions and uses the local login during development.
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={query}",
         "-f", f"login={USERNAME}", "-f", f"from={start}T00:00:00Z",
         "-f", f"to={today}T23:59:59Z"],
        capture_output=True, text=True, check=True, timeout=45,
    )
    payload = json.loads(result.stdout)
    if payload.get("errors"):
        raise ValueError("GitHub contribution query failed")
    weeks = payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    days = sorted(
        (day for week in weeks for day in week["contributionDays"]
         if str(start) <= day["date"] <= str(today)),
        key=lambda day: day["date"],
    )
    if len(days) != 31:
        raise ValueError("Expected 31 days of contribution data")

    left, right, top, bottom = 52, 868, 88, 228
    maximum = max(day["contributionCount"] for day in days)
    step = max(1, math.ceil(maximum / 4))
    ceiling = step * 4
    points = [(left + i * (right - left) / 30,
               bottom - day["contributionCount"] * (bottom - top) / ceiling)
              for i, day in enumerate(days)]
    path = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in points)
    total = sum(day["contributionCount"] for day in days)
    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="280" '
        'viewBox="0 0 900 280" role="img" aria-labelledby="title desc">',
        '<title id="title">GitHub activity over the last 31 days</title>',
        f'<desc id="desc">{total} contributions from {start} to {today}. '
        'Counts follow the GitHub contribution calendar.</desc>',
        '<rect width="900" height="280" rx="8" fill="#0d1117"/>',
        '<g font-family="Segoe UI, Arial, sans-serif">',
        '<text x="28" y="34" fill="#58a6ff" font-size="19" font-weight="600">GitHub activity</text>',
        f'<text x="28" y="58" fill="#8b949e" font-size="12">{total} contributions · last 31 days</text>',
    ]
    for i in range(5):
        y = bottom - i * (bottom - top) / 4
        svg += [
            f'<line x1="{left}" y1="{y}" x2="{right}" y2="{y}" stroke="#21262d"/>',
            f'<text x="40" y="{y + 4}" text-anchor="end" fill="#8b949e" font-size="11">{i * step}</text>',
        ]
    svg += [
        f'<path d="{path} L {right} {bottom} L {left} {bottom} Z" fill="#58a6ff" fill-opacity="0.10"/>',
        f'<path d="{path}" fill="none" stroke="#58a6ff" stroke-width="2.5" stroke-linejoin="round"/>',
    ]
    for day, (x, y) in zip(days, points):
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="#58a6ff">'
                   f'<title>{day["date"]}: {day["contributionCount"]} contributions</title></circle>')
    for i in (0, 5, 10, 15, 20, 25, 30):
        label = datetime.fromisoformat(days[i]["date"]).strftime("%b %d")
        svg.append(f'<text x="{points[i][0]:.1f}" y="251" text-anchor="middle" '
                   f'fill="#8b949e" font-size="11">{escape(label)}</text>')
    svg += ['</g>', '</svg>']
    save_svg("github-activity.svg", "\n".join(svg).encode())


def main():
    ASSETS.mkdir(exist_ok=True)
    jobs = [
        ("github-stats.svg", lambda: download_card(
            "github-stats.svg", "https://github-readme-stats.vercel.app/api",
            {"username": USERNAME, "show_icons": "true", "theme": "github_dark",
             "hide_border": "true", "hide_rank": "true", "disable_animations": "true"}, "Total Commits")),
        ("github-streak.svg", lambda: download_card(
            "github-streak.svg", "https://github-readme-streak-stats.herokuapp.com/",
            {"user": USERNAME, "theme": "github-dark-blue", "hide_border": "true",
             "disable_animations": "true"},
            "Current Streak")),
        ("github-activity.svg", activity_graph),
    ]
    failed = False
    for filename, generate in jobs:
        try:
            generate()
            print(f"Updated {filename}")
        except Exception as error:
            print(f"::warning::Could not update {filename}: {type(error).__name__}")
            if not (ASSETS / filename).exists():
                failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
