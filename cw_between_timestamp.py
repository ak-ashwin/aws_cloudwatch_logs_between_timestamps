# IF YOU INCUR HUGE COSTS WITH THIS OR IT BREAKS DON'T BLAME ME License

# This is a throw-away script I wrote to pull the json events for all of the streams from a cloudwatch log
# For some reason, the naive way to do vpc network logging does logging to different streams in a cloudwatch
# log based on interface.
# Great for diagnosing lots of things, and generating verbose logs, but for the broad-stroke analysis I was doing,
# all I really wanted was the basic data. This would have been easier if I had logged to s3, but I did not see a
# way to do that in 2 clicks.
from botocore.docs import paginator


group_name = '/aws/lambda/lms-tasks-handler-production'
start_time = 1547782200000
end_time = 1547785800000


import boto3, json, time

i = 0

client = boto3.client('logs')
kwargs = {}
while True:
    response = client.filter_log_events(
        logGroupName=group_name,
        startTime=start_time,
        endTime=end_time,
        **kwargs)
    """ do fancy stuff """
    if 'nextToken' not in response:
        break


    out_to = open(str(time.time()) + "cloud_logs.txt", 'w')
    out_to.write(json.dumps(response) + '\n')
    kwargs['nextToken'] = response['nextToken']
