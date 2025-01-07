from ec2_manager import EC2Manager
from s3_manager import S3Manager
from monitor import EC2Monitor


class CloudResourceManager:
    def __init__(self):
        self.ec2_manager = EC2Manager()
        self.s3_manager = S3Manager()
        self.ec2_monitor = EC2Monitor()

    def get_user_input(self, prompt, default=None, input_type=str):
        """Handles user input with optional default value and type conversion."""
        user_input = input(f"{prompt} (default: {default}): ").strip()
        if not user_input:
            return default
        try:
            return input_type(user_input)
        except ValueError:
            print(f"Invalid input. Expected {input_type.__name__}. Using default: {default}")
            return default

    def create_ec2_instance(self):
        """Prompts the user for necessary inputs to create an EC2 instance."""
        ami_id = self.get_user_input("Enter the AMI ID", "ami-01816d07b1128cd2d")
        instance_type = self.get_user_input("Enter the instance type", "t2.micro")
        key_name = self.get_user_input("Enter the key pair name", "vockey")
        security_group_ids_input = self.get_user_input(
            "Enter the security group IDs (comma-separated)", 'sg-0c8d1e7907882db8c'
        )
        security_group_ids = [
            sg.strip() for sg in security_group_ids_input.split(",")
        ]
        subnet_id = self.get_user_input("Enter the subnet ID", None)
        instance_profile = self.get_user_input("Enter the instance profile name", None)

        tags_input = self.get_user_input(
            "Enter tags as key:value pairs (comma-separated)", "Name:MyTestInstance44"
        )
        tags = [{"Key": kv.split(":")[0], "Value": kv.split(":")[1]} for kv in tags_input.split(",")]

        # Create EC2 instance
        instance_ids = self.ec2_manager.create_instance(
            ami_id=ami_id,
            instance_type=instance_type,
            key_name=key_name,
            security_group_ids=security_group_ids,
            subnet_id=subnet_id,
            instance_profile=instance_profile,
            tags=tags,
        )
        #print(f"Created EC2 Instance IDs: {instance_ids}")

    def terminate_ec2_instance(self):
        """Prompts the user to terminate an EC2 instance."""
        self.ec2_manager.list_instances()
        instance_id = input("Enter instance ID to terminate: ")
        self.ec2_manager.terminate_instance(instance_id)

    def manage_s3_bucket(self):
        """Manages S3 buckets: create, list, delete."""
        print("1. Create S3 Bucket")
        print("2. List S3 Buckets")
        print("3. Delete S3 Bucket")
        s3_choice = self.get_user_input("Choose an option for S3 management", 1, int)

        if s3_choice == 1:
            bucket_name = input("Enter bucket name: ")
            self.s3_manager.create_bucket(bucket_name)
        elif s3_choice == 2:
            self.s3_manager.list_buckets()
        elif s3_choice == 3:
            self.s3_manager.list_buckets()
            bucket_name = input("Enter bucket name to delete: ")
            self.s3_manager.delete_bucket(bucket_name)
        else:
            print("Invalid option, try again.")

    def monitor_ec2_instances(self):
        """Monitors EC2 instance metrics."""
        instance_id = input("Please enter the EC2 instance ID: ")
        self.ec2_monitor.list_instance_metrics(instance_id)

    def display_menu(self):
        """Displays the main menu for Cloud Resource Manager."""
        print("Cloud Resource Manager")
        print("1. Create EC2 Instance")
        print("2. List EC2 Instances")
        print("3. Terminate EC2 Instance")
        print("4. Manage S3 Buckets")
        print("5. Monitor EC2 Instances")
        print("6. Exit")

    def run(self):
        """Runs the main program loop."""
        while True:
            self.display_menu()
            choice = self.get_user_input("Enter your choice", 6, int)

            if choice == 1:
                self.create_ec2_instance()
            elif choice == 2:
                self.ec2_manager.list_instances()
            elif choice == 3:
                self.terminate_ec2_instance()
            elif choice == 4:
                self.manage_s3_bucket()
            elif choice == 5:
                self.monitor_ec2_instances()
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")


cloud_manager = CloudResourceManager()
cloud_manager.run()
