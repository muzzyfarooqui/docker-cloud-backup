import os

import boto3
from botocore.exceptions import ClientError


s3 = boto3.client(
    "s3",
    region_name="us-east-1"
)

bucket_name = "muzammil-cloud-storage-677296949574-us-east-1-an"


def object_exists(object_name):
    """Check whether an object exists in the AWS S3 bucket."""
    try:
        s3.head_object(
            Bucket=bucket_name,
            Key=object_name
        )
        return True

    except ClientError as error:
        error_code = error.response["Error"]["Code"]

        if error_code in ("404", "NoSuchKey", "NotFound"):
            return False

        raise


def upload_file():
    """Upload a local file to the AWS S3 bucket."""
    file_path = input("\nEnter the file name or path to upload: ")
    object_name = os.path.basename(file_path)

    try:
        s3.upload_file(
            file_path,
            bucket_name,
            object_name
        )

        print("\n==========================================")
        print("✅ Upload Successful")
        print("==========================================")
        print(f"File:   {object_name}")
        print(f"Bucket: {bucket_name}")

    except FileNotFoundError:
        print(f"\n❌ Upload Failed: '{file_path}' was not found on your computer.")
        print("Returning to main menu...")

    except Exception as error:
        print(f"\n❌ Upload Failed: {error}")
        print("Returning to main menu...")


def list_files():
    """List all objects stored in the AWS S3 bucket."""
    print("\nObjects in bucket:\n")

    try:
        response = s3.list_objects_v2(
            Bucket=bucket_name
        )

        if "Contents" not in response:
            print("Bucket is empty.")
            return

        for obj in response["Contents"]:
            print(f"• {obj['Key']}")

    except Exception as error:
        print(f"\n❌ Could not list files: {error}")
        print("Returning to main menu...")


def download_file():
    """Download an object from AWS S3 to the local project folder."""
    object_name = input("\nEnter the file name to download: ")

    if not object_exists(object_name):
        print(
            f"\n❌ Download Failed: "
            f"'{object_name}' does not exist in the bucket."
        )
        print("Returning to main menu...")
        return

    download_path = "downloaded_" + object_name

    try:
        s3.download_file(
            bucket_name,
            object_name,
            download_path
        )

        print("\n==========================================")
        print("✅ Download Successful")
        print("==========================================")
        print(f"File:     {object_name}")
        print(f"Saved as: {download_path}")

    except Exception as error:
        print(f"\n❌ Download Failed: {error}")
        print("Returning to main menu...")


def delete_file():
    """Delete an object from the AWS S3 bucket."""
    object_name = input("\nEnter the file name to delete: ")

    if not object_exists(object_name):
        print(
            f"\n❌ Delete Failed: "
            f"'{object_name}' does not exist in the bucket."
        )
        print("Returning to main menu...")
        return

    confirm = input(
        f"Are you sure you want to delete '{object_name}'? (y/n): "
    )

    if confirm.lower() != "y":
        print("\nDelete cancelled.")
        print("Returning to main menu...")
        return

    try:
        s3.delete_object(
            Bucket=bucket_name,
            Key=object_name
        )

        print("\n==========================================")
        print("✅ Delete Successful")
        print("==========================================")
        print(f"Deleted: {object_name}")

    except Exception as error:
        print(f"\n❌ Delete Failed: {error}")
        print("Returning to main menu...")


def show_menu():
    """Display the main application menu."""
    print("\n==========================================")
    print("      Cloud Object Storage Client")
    print("==========================================")
    print(f"Current Bucket: {bucket_name}")
    print("------------------------------------------")
    print("1. Upload File")
    print("2. List Files")
    print("3. Download File")
    print("4. Delete File")
    print("5. Exit")
    print("==========================================")


while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        upload_file()

    elif choice == "2":
        list_files()

    elif choice == "3":
        download_file()

    elif choice == "4":
        delete_file()

    elif choice == "5":
        print("\n👋 Thanks for using Cloud Object Storage Client!")
        break

    else:
        print(
            "\n❌ Invalid option. "
            "Please choose a number between 1 and 5."
        )
        print("Returning to main menu...")