#!/usr/bin/env python
"""What is Gregg Wallace doing?

A web app that let's you know what Gregg Wallace is up to based on his interview in The
Torygraph.

This program is free software: you can redistribute it and/or modify it under the terms
of the GNU Affero General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this
program.  If not, see <http://www.gnu.org/licenses/>.
"""

__copyright__ = "Copyright (C) 2024  Mike Coats"
__license__ = "AGPL-3.0-or-later"
__contact__ = "i.am@mikecoats.com"

__author__ = "Mike Coats"
__credits__ = ["Mike Coats", "Gregg Wallace"]

__maintainer__ = "Mike Coats"
__email__ = "i.am@mikecoats.com"

__status__ = "Production"
__version__ = "1.0.2"

import asyncio
from datetime import datetime

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

schedule_entries = [
    [
        0,
        500,
        """
        sleeping, stirring. Getting ready to inflict himself on the world, or Kent at
        least.""",
    ],
    [
        500,
        600,
        """
        reading a book he thinks will make him sound intellectual.""",
    ],
    [
        600,
        700,
        """
        drinking coffee and checking emails. He's just like you! So relatable.""",
    ],
    [
        700,
        730,
        """
        demanding Gym staff get in and open up early so he doesn't have to swim with the
        proles.""",
    ],
    [
        730,
        1030,
        """
        living his best #influencer life, ticking off his to-do list while walking off his bloated belly. #hustle""",
    ],
    [
        1030,
        1200,
        """
        forcing his PA to eat a cooked breakfast with him at a Harvester. It's not grim,
        honest! They do grilled chicken!""",
    ],
    [
        1200,
        1330,
        """
        eating lunch prepared by his current, and fourth, wife.""",
    ],
    [
        1330,
        1500,
        """
        grudgingly spending time with his unwanted, disabled, son.""",
    ],
    [
        1500,
        1700,
        """
        playing computer games, like all good historians.""",
    ],
    [
        1700,
        1800,
        """
        not telling! Nobody knows. It's his special secret time. Shh!""",
    ],
    [
        1800,
        2000,
        """
        cooking dinner and drinking. Not excessively, mind. Just a pint of beer, then
        some wine and then maybe a whisky or a brandy.""",
    ],
    [
        2000,
        2100,
        """
        watching films on his laptop in bed. Definitely not sitting on the sofa eating
        biscuits like you plebs.""",
    ],
    [
        2100,
        2400,
        """
        soundly sleeping. Safe in the knowledge he's made an impact on the people around
        him.""",
    ],
]


def get_schedule(hour_min_stamp: int) -> str:
    """Determine where we are in Gregg's schedule from the time of day."""
    schedule = ""

    for entry in schedule_entries:
        if entry[0] <= hour_min_stamp < entry[1]:
            schedule = entry[2]

    return schedule


app = FastAPI()
templates = Jinja2Templates(directory=".")
app.mount("/assets", StaticFiles(directory="./assets"), name="assets")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Return an HTML page so our visitor knows what Gregg's doing."""
    now = datetime.now()
    hour_min_stamp = now.hour * 100 + now.minute
    schedule = get_schedule(hour_min_stamp)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "time": f"{now.hour}:{now.minute}", "schedule": schedule},
    )


async def main():
    """When the module is run directly, hook up a uvicorn server and host the app."""
    config = uvicorn.Config("main:app", host="0.0.0.0", port=8002, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
