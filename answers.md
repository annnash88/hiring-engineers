## Support Engineer Datadog Challenge   

### Set-up  
I chose to implement Datadog using an Ubuntu Virtual Machine(VM) using the suggested [Vagrant VM service.](https://www.vagrantup.com/intro/getting-started/install.html) All terminal commands listed in this file are formatted for Linux machines. For directions on installing the Agent for Ubuntu [click here.](https://app.datadoghq.com/account/settings#agent/ubuntu) After installation, basic Agent usage for Ubuntu can be found [here.](https://docs.datadoghq.com/guides/basic_agent_usage/ubuntu/)

### Collecting Data  
**Bonus question: In your own words, what is the Agent?** 
Once installed, the Datadog Agent acts like a messenger by collecting information (events & metrics) from your host(s) and delivering it to Datadog. That data is then able to be catalogued, analyzed and monitored using customizable features in the Datadog UI. Official description can be found by reading the [Basic Agent Usage doc.](https://docs.datadoghq.com/guides/basic_agent_usage/)

**Add tags in the Agent config file and show us a screenshot of your host and its tags on the Host Map page in Datadog.**  
The Agent config file is located at `/etc/dd-agent/datadog.conf`.
I opted to use Linux's in-line file editor nano for my additions. Below is an in-terminal view of the custom tags I added.

##### datadog.conf custom tags  
![datadog.conf file terminal view](https://github.com/annnash88/hiring-engineers/blob/master/conf-tags.png?raw=true)  

Access my code file by [clicking here & scroll to line 32 for custom tags.](hiring-engineers/support-engineer-code/datadog.conf)  

After making changes to the datadog.conf file, restart the Agent by using the following command:   
`sudo /etc/init.d/datadog-agent restart`. Within a few minutes, the Datadog UI host map should synch up with your modified host. On the Host map click on your modified host and you will see the custom tags you added to the datadog.conf file as seen below on the far-right.

##### Host map detail view with custom tags 
![Hostmap & Tags](https://github.com/annnash88/hiring-engineers/blob/master/hostmaptags.png?raw=true
)
[Click here for my dashboard](https://app.datadoghq.com/infrastructure/map?fillby=avg%3Acpuutilization&sizeby=avg%3Anometric&groupby=none&nameby=name&nometrichosts=false&tvMode=false&nogrouphosts=false&palette=green_to_orange&paletteflip=false)


**Install a database on your machine (MongoDB, MySQL, or PostgreSQL) and then install the respective Datadog integration for that database.**  

To browse the available database integrations Datadog offers, go to the Datadog UI and scroll to the puzzle-piece/Integrations tab on the left-hand side and select "Integrations" from the dropdown menu. After that, use the search bar to see if your favorite database(db) is featured. Once you locate your desired db integration, click on the install button and instructions will pop-up and walk you through adding the integration. More information on integrations can be found [here.](https://docs.datadoghq.com/integrations)

##### Instructions detail for MySql Integration  
![MySql Integration Install Instructions](https://github.com/annnash88/hiring-engineers/blob/master/mysql-int.png?raw=true)

To configure your MySql db follow [these instructions.](https://docs.datadoghq.com/integrations/mysql/)
To connect your db with the Agent, you will need to create a `mysql.yaml` in the `conf.d` directory. You can find my code file example by [clicking here.](https://github.com/annnash88/hiring-engineers/blob/master/mysql.yaml)

*Please note, a working `mysql.yaml` file will have `<UNIQUEPASSWORD>` switched out with the password generated in step 1 of the db configuration instructions.*

##### Write a custom Agent check that samples a random value. Call this new metric: test.support.random  
To create a custom Agent Check, you will need to add a `name.py` to your `checks.d` directory, and a `name.yaml` to your `conf.d` directory. Both files must share the same 'name.' You can see my [yaml code file here](https://github.com/annnash88/hiring-engineers/blob/master/my_check.yaml), and my [py code here.](https://github.com/annnash88/hiring-engineers/blob/master/my_check.py) Detailed Agent Check docs can be found [here.](https://docs.datadoghq.com/guides/agent_checks/)

###### Python check file test.support.random code to sample random number < 1  
```python
from checks import AgentCheck
import random
class SupportRando(AgentCheck):
    def check(self, instance):
        self.gauge('test.support.random', random.random())
```
### Visualizing Data  
**Clone your database integration dashboard and add additional database metrics to it as well as your test.support.random metric from the custom Agent check.** 

I used the following article to help me with cloning my db Dashboard - [MySql Monitoring with Datadog.](https://www.datadoghq.com/blog/mysql-monitoring-with-datadog/) For general information, click [Dashboard Templating.](https://docs.datadoghq.com/guides/templating/)

###### Successfully cloned MySql db & custom Agent Check metric  
![Cloned database and custom metrics](https://github.com/annnash88/hiring-engineers/blob/master/dashboard-variables.png?raw=true)  
[Click for my cloned db Dashboard](https://app.datadoghq.com/dash/375720/custom-metrics---mysql-cloned?live=true&page=0&is_auto=false&from_ts=1507573147890&to_ts=1507576747890&tile_size=m)

**Bonus question: What is the difference between a timeboard and a screenboard?**  

There are several differences between Timeboards and Screenboards, but the biggest difference is that the Screenboard is a much more flexible and comprehensive dashboard. Screenboards allow the user to compile a dashboard from drag and drop widgets that can monitor data with different timeframes, and the entire board can be shared.

Timeboards are more rigid, and require that all graphs depict the same timeframe. Timeboards cannot be shared as a whole - only specific graphs from a Timeboard can be shared at a time. This makes Timeboards especially helpful for troubleshooting.

For more information on Timeboard vs. Screenboard [click here.](https://help.datadoghq.com/hc/en-us/articles/204580349-What-is-the-difference-between-a-ScreenBoard-and-a-TimeBoard-)


**Take a snapshot of your test.support.random graph and draw a box around a section that shows it going above 0.90. Make sure this snapshot is sent to your email by using the @notification**  

On my Dashboard, I clicked on my Test Support Random graph's camera-icon to create an annotation. Because this is not a monitor, I was not able to use `@notification` to send myself an email, but I was able to send the annotation to a friend who then forwarded me the message. You can read more about [@notification capabilities here.](https://help.datadoghq.com/hc/en-us/articles/203038119-What-do-notifications-do-in-Datadog-)

###### Annotation comment  
![Graph & graph comment](https://github.com/annnash88/hiring-engineers/blob/master/testsuprando-graph.png?raw=true)

###### Annotation email sent to friend  
![Graph comment email](https://github.com/annnash88/hiring-engineers/blob/master/graph-notification.png?raw=true)

### Alerting on Data  
**Set up a monitor on this metric that alerts you when it goes above 0.90 at least once during the last 5 minutes**  

I set-up my monitor by clicking on my graph's "More Actions" cog-wheel and clicked "Create Monitor." Detailed instructions on creating monitors can be [found here.](https://docs.datadoghq.com/guides/monitors/)

###### Simple alert monitor configuration
![Monitor Conditions](https://github.com/annnash88/hiring-engineers/blob/master/monitor-alert-conditions.png?raw=true)

###### Simple alert monitor email
![Monitor simple alert](https://github.com/annnash88/hiring-engineers/blob/master/monitor-simple-alert.png?raw=true)  

[Click here for my simple alert monitor](https://app.datadoghq.com/monitors#2996606?group=all&live=4h)

**Bonus points: Make it a multi-alert by host so that you won't have to recreate it if your infrastructure scales up.**  

Changing the alert from simple to multi is easy, and can be done by editing step 2 of your monitor configuration.

###### Multi alert monitor configuration
![Multi-alert](https://github.com/annnash88/hiring-engineers/blob/master/multi-alert-host.png?raw=true)

**This monitor should alert you within 15 minutes. So when it does, take a screenshot of the email that it sends you.**  
###### Multi alert monitor email

![Multi-alert email](https://github.com/annnash88/hiring-engineers/blob/master/multi-host-alert-msg.png?raw=true)

**Bonus: Set up a scheduled downtime for this monitor that silences it from 7pm to 9am daily. Make sure that your email is notified when you schedule the downtime and take a screenshot of that notification.**  

Downtimes can be managed by clicking on the Monitor's dropdown list and selecting "Manage Downtime." Once redirected to the Manage Downtime screen, click on "Schedule Downtime."

###### Scheduling downtime
![Downtime configuration](https://github.com/annnash88/hiring-engineers/blob/master/downtime-config.png?raw=true)

###### Email notification for scheduled downtime
![Downtime notification email](https://github.com/annnash88/hiring-engineers/blob/master/downtime-email.png?raw=true)

*Email notification shows 9:00pm - 9:00am, since I was coding past the 7:00pm starttime my Downtime message was not triggered.*
