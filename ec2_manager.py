import boto3

class EC2Manager:
    def __init__(self):
        self.ec2_client = boto3.client("ec2")
        self.ec2_resource = boto3.resource("ec2")

    def create_instance(
        self,
        ami_id,
        security_group_ids,
        instance_type="t2.micro",
        key_name="vockey",
        min_count=1,
        max_count=1,
        user_data=None,
        instance_profile=None,
        subnet_id=None,
        tags=None,
    ):
        """
        Create an EC2 instance with the specified parameters.
        """
        try:
            run_instances_params = {
                "BlockDeviceMappings": [
                    {
                        "DeviceName": "/dev/xvda",
                        "Ebs": {
                            "VolumeSize": 30,
                            "VolumeType": "gp2",
                            "DeleteOnTermination": True,
                        },
                    },
                ],
                "ImageId": ami_id,
                "InstanceType": instance_type,
                "KeyName": key_name,
                "MinCount": min_count,
                "MaxCount": max_count,
                "SecurityGroupIds": security_group_ids,
            }

            if tags:
                run_instances_params["TagSpecifications"] = [
                    {"ResourceType": "instance", "Tags": tags}
                ]

            if user_data:
                run_instances_params["UserData"] = user_data

            if instance_profile:
                run_instances_params["IamInstanceProfile"] = {"Name": instance_profile}

            if subnet_id:
                run_instances_params["SubnetId"] = subnet_id

            response = self.ec2_client.run_instances(**run_instances_params)

            instance_ids = [instance["InstanceId"] for instance in response["Instances"]]
            print(f"Created EC2 instance(s): {', '.join(instance_ids)}")
            return instance_ids

        except Exception as e:
            print(f"Error creating instance: {str(e)}")
            return None

    def list_instances(self):
        """
        List all EC2 instances with their details.
        """
        try:
            instances = self.ec2_client.describe_instances()
            for reservation in instances["Reservations"]:
                for instance in reservation["Instances"]:
                    instance_id = instance["InstanceId"]
                    state = instance["State"]["Name"]
                    name = None
                    if "Tags" in instance:
                        for tag in instance["Tags"]:
                            if tag["Key"] == "Name":
                                name = tag["Value"]
                                break
                    print(
                        f"Instance ID: {instance_id}, Name: {name if name else 'No Name'}, State: {state}"
                    )
        except Exception as e:
            print(f"Error listing instances: {str(e)}")

    def terminate_instance(self, instance_id):
        """
        Terminate an EC2 instance by its instance ID.
        """
        try:
            self.ec2_client.terminate_instances(InstanceIds=[instance_id])
            print(f"Terminated EC2 instance {instance_id}")
        except Exception as e:
            print(f"Error terminating instance: {str(e)}")


