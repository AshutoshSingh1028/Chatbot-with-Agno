from typing import List, Dict, Any, Literal, Optional
from datetime import date, datetime, timedelta
from collections import defaultdict
from agno.tools import Toolkit

class FinanceToolkit(Toolkit):
    def __init__(self):
        super().__init__(name="finance_toolkit")
        self.register(expense_summary)

def expense_summary(
    period: Literal["daily", "weekly", "monthly"],
    items: List[Dict[str, Any]],
    start_date: Optional[str] = None,  # ISO "YYYY-MM-DD"; optional anchor
) -> str:
    """
    Summarize expenses by category over a daily/weekly/monthly window.

    Args:
      - period: "daily" | "weekly" | "monthly"
      - items: [{"date": "YYYY-MM-DD", "category": "food|rent|travel|...", "amount": number}, ...]
      - start_date (optional): window anchor; defaults to today for daily/weekly,
        and first of current month for monthly.

    Returns:
      Markdown string with category totals and a grand total.

    Example:
      Here’s a concise 5-day Tokyo trip plan for 2 people within a $3000 budget ($1500 per person):                                            ┃
┃                                                                                                                                          ┃
┃                                                           Itinerary Highlights                                                           ┃
┃                                                                                                                                          ┃
┃    1 Day 1: Explore Shinjuku (Skytree, nightlife) + stay at budget hotel (e.g., OYO Shinjuku Hotel, $60/night).                            ┃
┃    2 Day 2: Harajuku & Shibuya (shopping, scramble crossing) + dinner at local yakitori spot ($50 for two).                                ┃
┃    3 Day 3: Asakusa & Senso-ji Temple ($10 entry) + visit Tsukiji Fish Market (breakfast at sushi stalls for $15).                         ┃
┃    4 Day 4: Akihabara (electronics, anime culture) + Imperial Palace Gardens (free entry).                                                 ┃
┃    5 Day 5: Shibuya (TeamLab Planets digital art, $30/person) + day trip to Hakone (volcano views, hot springs, $300 for shuttle + 4-5hr   ┃
┃      trip).                                                                                                                                ┃
┃                                                                                                                                          ┃
┃                                                             Budget Breakdown                                                             ┃
┃                                                                                                                                          ┃
┃    • Flights: $1200 (e.g., round-trip from North America in December).                                                                     ┃
┃    • Accommodation: $600 (3-star capsule hotels or budget chains).                                                                         ┃
┃    • Food: $400 (mix $15-30 meals, sushi, ramen).                                                                                          ┃
┃    • Activities: $500 (TeamLab, Skytree, local transit passes).                                                                            ┃
┃                                                                                                                                          ┃
┃                                                                   Tips                                                                   ┃
┃                                                                                                                                          ┃
┃    • Use Suica/Pasmo cards for public transport (avoid taxi costs).                                                                        ┃
┃    • Pre-book popular attractions (TeamLab Planets requires advance tickets).                                                              ┃
┃    • Visit Tsukiji Outer Market for affordable souvenirs and street food.
    """
    def parse(d: str) -> date:
        return datetime.fromisoformat(d).date()

    today = date.today()

    if period == "daily":
        start = parse(start_date) if start_date else today
        end = start
        title = f"Expense Summary (Daily)"
    elif period == "weekly":
        anchor = parse(start_date) if start_date else today
        # align to Monday
        start = anchor - timedelta(days=anchor.weekday())
        end = start + timedelta(days=6)
        title = f"Expense Summary (Weekly)"
    else:  # monthly
        if start_date:
            anchor = parse(start_date).replace(day=1)
        else:
            anchor = today.replace(day=1)
        start = anchor
        # next month start
        if anchor.month == 12:
            next_month = anchor.replace(year=anchor.year + 1, month=1, day=1)
        else:
            next_month = anchor.replace(month=anchor.month + 1, day=1)
        end = next_month - timedelta(days=1)
        title = f"Expense Summary (Monthly)"

    totals = defaultdict(float)
    grand = 0.0

    for it in items:
        try:
            d = parse(str(it["date"]))
            cat = str(it["category"]).strip().lower()
            amt = float(it["amount"])
        except Exception:
            continue
        if start <= d <= end:
            totals[cat] += amt
            grand += amt

    lines = [
        f"# {title}",
        f"- Period: {start.isoformat()} → {end.isoformat()}",
        "",
        "## Totals by Category",
    ]
    if totals:
        for cat, amt in sorted(totals.items()):
            lines.append(f"- {cat}: ₹{amt:,.2f}")
    else:
        lines.append("- No expenses in this period.")

    lines += ["", "## Grand Total", f"- ₹{grand:,.2f}"]
    return "\n".join(lines)
