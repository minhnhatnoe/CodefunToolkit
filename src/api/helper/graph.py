from io import BytesIO

from datetime import datetime, timedelta
import matplotlib.pyplot as plt

from . import getsub
from ..models import Submission

def get_startend(submissions: list[Submission]) -> tuple[datetime, datetime]:
    start_time = submissions[-1].submit_timestamp_notz
    start_time = start_time.replace(hour=0, minute=0, second=0, microsecond=0)
    
    end_time = submissions[0].submit_timestamp_notz
    end_time = end_time.replace(hour=0, minute=0, second=0, microsecond=0)
    end_time += timedelta(days=1)
    return start_time, end_time


async def make_graph(user: str, xcnt: int = 30, ycnt: int = 10) -> bytes | None:
    '''Generate a graph representing a user's learning rate'''
    submissions = await getsub.get_submissions(user)
    if len(submissions) == 0: return None

    start_time, end_time = get_startend(submissions)
    time_period = (end_time-start_time).days
    time_per_col: int
    if time_period < xcnt:
        xcnt = time_period
        time_per_col = 1
    else:
        time_per_col = (time_period-1) // xcnt + 1
    
    sub_ptr = len(submissions)-1
    time_points = []
    values = []
    for i in range(xcnt):
        range_end_time = start_time + timedelta(days=(i+1)*time_per_col)
        time_points.append(range_end_time)
        values.append([0, 0, 0])
        while sub_ptr >= 0 and \
        submissions[sub_ptr].submit_timestamp_notz < range_end_time:
            values[-1][0] += 1
            if submissions[sub_ptr].isScored:
                values[-1][1] += 1
                if submissions[sub_ptr].result == "AC":
                    values[-1][2] += 1
            sub_ptr -= 1
    print(start_time)
    fig, ax = plt.subplots()
    ax.plot(time_points, values)
    ax.set_title(user)

    ax.tick_params('x', rotation=45)

    max_per_day = max(map(max, values))
    ax.set_yticks(range(0, max_per_day, max_per_day//ycnt))

    ax.legend(['All', 'Scored', 'Accepted'])
    ax.grid(True)

    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    return buffer.getvalue()
