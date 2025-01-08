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
            print(f"\n[ERROR] Invalid input. Expected {input_type.__name__}. Using default: {default}\n")
            return default

    def create_ec2_instance(self):
        """Prompts the user for necessary inputs to create an EC2 instance."""
        print("\n=== Create EC2 Instance ===")
        ami_id = self.get_user_input("Enter the AMI ID", "ami-01816d07b1128cd2d")
        instance_type = self.get_user_input("Enter the instance type", "t2.micro")
        key_name = self.get_user_input("Enter the key pair name", "vockey")
        security_group_ids_input = self.get_user_input(
            "Enter the security group IDs (comma-separated)", None
        )
        if security_group_ids_input:
            security_group_ids = [
                sg.strip() for sg in security_group_ids_input.split(",")
            ]
        else:
            security_group_ids=None

        subnet_id = self.get_user_input("Enter the subnet ID", None)
        instance_profile = self.get_user_input("Enter the instance profile name", None)

        tags_input = self.get_user_input(
            "Enter tags as key:value pairs (comma-separated)", "Name:MyTestInstance"
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


    def terminate_ec2_instance(self):
        """Prompts the user to terminate an EC2 instance."""
        print("\n=== Terminate EC2 Instance ===")
        self.ec2_manager.list_instances()
        instance_id = input("Enter instance ID to terminate: ").strip()
        self.ec2_manager.terminate_instance(instance_id)
        print(f"\n[INFO] Terminated EC2 Instance: {instance_id}\n")

    def manage_s3_bucket(self):
        """Manages S3 buckets: create, list, delete."""
        print("\n=== Manage S3 Buckets ===")
        print("1. Create S3 Bucket")
        print("2. List S3 Buckets")
        print("3. Delete S3 Bucket")
        s3_choice = self.get_user_input("Choose an option for S3 management", 1, int)

        if s3_choice == 1:
            bucket_name = input("Enter bucket name: ").strip()
            self.s3_manager.create_bucket(bucket_name)
            print(f"\n[INFO] S3 Bucket '{bucket_name}' created successfully.\n")
        elif s3_choice == 2:
            print("\n[INFO] Listing S3 Buckets:")
            self.s3_manager.list_buckets()
        elif s3_choice == 3:
            print("\n[INFO] Listing S3 Buckets:")
            self.s3_manager.list_buckets()
            bucket_name = input("Enter bucket name to delete: ").strip()
            self.s3_manager.delete_bucket(bucket_name)
            print(f"\n[INFO] S3 Bucket '{bucket_name}' deleted successfully.\n")
        else:
            print("\n[ERROR] Invalid option. Try again.\n")

    def monitor_ec2_instances(self):
        """Monitors EC2 instance metrics."""
        print("\n=== Monitor EC2 Instances ===")
        instance_id = input("Enter the EC2 instance ID: ").strip()
        self.ec2_monitor.list_instance_metrics(instance_id)

    def display_menu(self):
        """Displays the main menu for Cloud Resource Manager."""
        print("\n=== Cloud Resource Manager ===")
        print("1. Create EC2 Instance")
        print("2. List EC2 Instances")
        print("3. Terminate EC2 Instance")
        print("4. Manage S3 Buckets")
        print("5. Monitor EC2 Instances")
        print("6. Exit")
        print("=" * 30)

    def run(self):
        """Runs the main program loop."""
        while True:
            self.display_menu()
            choice = self.get_user_input("Enter your choice", 6, int)

            if choice == 1:
                self.create_ec2_instance()
            elif choice == 2:
                print("\n=== List EC2 Instances ===")
                self.ec2_manager.list_instances()
            elif choice == 3:
                self.terminate_ec2_instance()
            elif choice == 4:
                self.manage_s3_bucket()
            elif choice == 5:
                self.ec2_manager.list_instances()
                self.monitor_ec2_instances()
            elif choice == 6:
                print("\n[INFO] Exiting Cloud Resource Manager. Goodbye!\n")
                break
            else:
                print("\n[ERROR] Invalid choice. Try again.\n")


cloud_manager = CloudResourceManager()
cloud_manager.run()
