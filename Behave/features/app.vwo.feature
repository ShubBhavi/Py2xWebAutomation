Feature:Searching the APP.VWO.COM
  Scenario Outline: search the app.vwo.com
    Given open the app.vwo.com
    When I enter the <username> and <password>
    Then I get the <message>
    Examples:
      | username  | password  | message                                                   |
      | admin     | admin     |Your email, password, IP address or location did not match |
      | admin1    | password  |Your email, password, IP address or location did not match |
      | admin2    | password  |Your email, password, IP address or location did not match |

