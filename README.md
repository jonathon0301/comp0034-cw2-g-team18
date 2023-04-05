# COMP0034 Coursework 2

This repository is created for COMP0034 Coursework 2 done by Team 18. This README.md will provide introduce our 
developed REST API, which enables users to check gender pay gap data from their desired perspective. It will also talk 
about how we tested the developed app with evidence of work.

## Set-up instructions
1. URL to the GitHub repository: https://github.com/ucl-comp0035/comp0034-cw2-g-team18.git ;
2. Please install all necessary Python packages listed in [requirements.txt](requirements.txt);
3. Browser used to test the Dash created in this coursework is Chrome 109 version and our group members use Mac OS, 
the chromedriver is downloaded to [chromedriver_mac_arm64](test/chromedriver_mac_arm64) directory under [test](test) 
folder. You may need to execute it first before going to testing;
4. The CI workflow was implemented by changing some default settings of GitHub Python application. The document can be 
seen in [python-app.yml](.github/workflows/python-app.yml). Linting and dependency management can also be seen from it.

## 1. Gender Pay Gap REST API
We have developed a REST API which allows users to check relevant gender pay gap situation data that they wish to have a
 look at from their desired viewpoint (from a certain industry, region, or employer size). 