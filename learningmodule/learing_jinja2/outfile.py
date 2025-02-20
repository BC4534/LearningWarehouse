from lib2to3.fixes.fix_input import context

import requests
import pytest
from Tools.scripts.generate_opcode_h import header


class TestLogin:



    def test_http___47_111_104_162_30301_web_api_open_login(self):
        response = requests.request(
            method = 'POST',
            url = 'http://47.111.104.162:30301/web-api/open/login',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInJlZ2lvbnMiOltdLCJyb2xlcyI6WyJKUzAwMDEiXSwiaXNzIjoic2VsZiIsIm5hbWUiOiLns7vnu5_nrqHnkIblkZgiLCJleHAiOjE3MzQ2ODYyMTUsImlhdCI6MTczNDU5OTgxNSwiZ3JvdXAiOiJHTE9CQUxfTUFOQUdFUiJ9.U7eVo_EmCxDtj5ghQV0j0zOCpr-2dHbx0n9x5O9wtymdtzpdqL-9C9eOqdLebGnEl3qhlSdElSHXqdUiUJUg5VSXXlZsm4eKXKUOaQ5Dvder7n1_GUTbfgVW33EX7IgaJfBOIISXLbEFi2PgrXVxJrFhfHkVm8tGUyXR1CznAAFUsDkZOWLMhJGObbeybLKpNyXLtp_WPDqxjEwEtYI5R1X3kRt4cEYacgBf59gT_SunJAyU2cbzpm0CpUN6MrORCxxMLj7GqEFSWBWv1MPekwhRW4oocCyvCkk-6_halqqyS9vMpmWWPSUkT6Axnq4v0bS82f6p3S2HfzMUlWq9lw'
            },
            json = {"username":"admin","password":"1234566"})
        assert response.status_code == 200

    def test_http___47_111_104_162_30301_web_api_open_login(self):
        response = requests.request(
            method = 'POST',
            url = 'http://47.111.104.162:30301/web-api/open/login',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInJlZ2lvbnMiOltdLCJyb2xlcyI6WyJKUzAwMDEiXSwiaXNzIjoic2VsZiIsIm5hbWUiOiLns7vnu5_nrqHnkIblkZgiLCJleHAiOjE3MzQ2ODYyMTUsImlhdCI6MTczNDU5OTgxNSwiZ3JvdXAiOiJHTE9CQUxfTUFOQUdFUiJ9.U7eVo_EmCxDtj5ghQV0j0zOCpr-2dHbx0n9x5O9wtymdtzpdqL-9C9eOqdLebGnEl3qhlSdElSHXqdUiUJUg5VSXXlZsm4eKXKUOaQ5Dvder7n1_GUTbfgVW33EX7IgaJfBOIISXLbEFi2PgrXVxJrFhfHkVm8tGUyXR1CznAAFUsDkZOWLMhJGObbeybLKpNyXLtp_WPDqxjEwEtYI5R1X3kRt4cEYacgBf59gT_SunJAyU2cbzpm0CpUN6MrORCxxMLj7GqEFSWBWv1MPekwhRW4oocCyvCkk-6_halqqyS9vMpmWWPSUkT6Axnq4v0bS82f6p3S2HfzMUlWq9lw'
            },
            json = {"username":"admin","password":"12345664"})
        assert response.status_code == 200
