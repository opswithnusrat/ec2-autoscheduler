import boto3

REGION = xxxxxxxx  # Change to your AWS region
TAG_KEY = 'AutoSchedule'
TAG_VALUE = 'true'

def lambda_handler(event, context):
    action = event.get("action", "stop")  # 'start' or 'stop'
    ec2 = boto3.client('ec2', region_name=REGION)

    # Filter EC2 instances by tag and state
    response = ec2.describe_instances(
        Filters=[
            {"Name": f"tag:{TAG_KEY}", "Values": [TAG_VALUE]},
            {"Name": "instance-state-name", "Values": ["running" if action == "stop" else "stopped"]}
        ]
    )

    instance_ids = [
        instance["InstanceId"]
        for reservation in response["Reservations"]
        for instance in reservation["Instances"]
    ]

    if not instance_ids:
        print(f"No instances to {action}.")
        return

    print(f"{action.capitalize()}ping instances: {instance_ids}")
    if action == "stop":
        ec2.stop_instances(InstanceIds=instance_ids)
    elif action == "start":
        ec2.start_instances(InstanceIds=instance_ids)