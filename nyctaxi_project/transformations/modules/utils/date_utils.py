from datetime import date
import re
from dateutil.relativedelta import relativedelta

def get_target_yyyymm(months_ago: int = 4) -> str:
    """
    Returns the year-month string in (yyyy-MM) format for given number of months ago.
    """
    target_date = date.today() - relativedelta(months=months_ago)
    return target_date.strftime("%Y-%m")

def get_month_start_n_months_ago(months_ago: int = 4) -> date:
    """
    Returns the date representing the first day of the n month
    """
    return date.today().replace(day=1) - relativedelta(months=months_ago)