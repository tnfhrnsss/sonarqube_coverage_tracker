# sonarqube code coverage tracker

This project monitors code coverage measured in SonarQube to help maintain quality.


## Requirements

* python 3.12+
* slack-sdk


## Usage

* You can configure the sonarqube api url and Slack details in the env.json.
     ```
      {
        "slack_token": "",
        "slack_channel_id": "",
        "projects": [],
        "sonarqube": {
          "api_url": "http://localhost:9100/api"
        }
      }
      ```

## Output snapshot
* slack message
  
    ![slack_message](https://tnfhrnsss.github.io/docs/sub-projects/img/sonarqube_coverage_monitoring.png)


## Blog reference

For further reference, please consider the following sections:

* [blog](https://tnfhrnsss.github.io/docs/sub-projects/sonarqube_coverage_monitoring/)

