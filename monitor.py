import boto3

class EC2Monitor:
    def __init__(self):
        self.cloudwatch = boto3.client('cloudwatch')

    def list_instance_metrics(self, instance_id):
        try:
            # List EC2 metrics for the specified instance ID
            print(f"Retrieving metrics for instance: {instance_id}")
            metrics = self.cloudwatch.list_metrics(
                Namespace='AWS/EC2',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}]
            )

            if not metrics['Metrics']:
                print(f"No metrics found for instance {instance_id}")
                return

            # Print out the metrics for the specified EC2 instance
            for metric in metrics["Metrics"]:
                metric_name = metric['MetricName']
                dimensions = metric['Dimensions']
                print(f"Metric Name: {metric_name}, Dimensions: {dimensions}")
        except Exception as e:
            print(f"Error retrieving metrics for instance {instance_id}: {str(e)}")


