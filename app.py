from minio import Minio
from minio.error import S3Error


# MinIO connection settings
client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="password123",
    secure=False
)

bucket_name = "docker-cloud-backup"


def object_exists(object_name):
    """Check if an object exists in the bucket."""
    try:
        objects = client.list_objects(bucket_name)

        for obj in objects:
            if obj.object_name == object_name:
                return True

        return False

    except S3Error:
        return False


def upload_file():
    """Upload a local file to the MinIO bucket."""
    file_path = input("\nEnter the file name to upload: ")
    object_name = file_path

    try:
        client.fput_object(bucket_name, object_name, file_path)

        print("\n==========================================")
        print("✅ Upload Successful")
        print("==========================================")
        print(f"File:   {object_name}")
        print(f"Bucket: {bucket_name}")

    except FileNotFoundError:
        print(f"\n❌ Upload Failed: '{file_path}' was not found on your computer.")
        print("Returning to main menu...")

    except S3Error as error:
        print(f"\n❌ Upload Failed: {error}")
        print("Returning to main menu...")


def list_files():
    """List all objects stored in the MinIO bucket."""
    print("\nObjects in bucket:\n")

    try:
        objects = client.list_objects(bucket_name)
        found = False

        for obj in objects:
            print(f"• {obj.object_name}")
            found = True

        if not found:
            print("Bucket is empty.")

    except S3Error as error:
        print(f"\n❌ Could not list files: {error}")
        print("Returning to main menu...")


def download_file():
    """Download an object from MinIO to the local project folder."""
    object_name = input("\nEnter the file name to download: ")
    download_path = "downloaded_" + object_name

    if not object_exists(object_name):
        print(f"\n❌ Download Failed: '{object_name}' does not exist in the bucket.")
        print("Returning to main menu...")
        return

    try:
        client.fget_object(bucket_name, object_name, download_path)

        print("\n==========================================")
        print("✅ Download Successful")
        print("==========================================")
        print(f"File:     {object_name}")
        print(f"Saved as: {download_path}")

    except S3Error as error:
        print(f"\n❌ Download Failed: {error}")
        print("Returning to main menu...")


def delete_file():
    """Delete an object from the MinIO bucket."""
    object_name = input("\nEnter the file name to delete: ")

    if not object_exists(object_name):
        print(f"\n❌ Delete Failed: '{object_name}' does not exist in the bucket.")
        print("Returning to main menu...")
        return

    confirm = input(f"Are you sure you want to delete '{object_name}'? (y/n): ")

    if confirm.lower() != "y":
        print("\nDelete cancelled.")
        print("Returning to main menu...")
        return

    try:
        client.remove_object(bucket_name, object_name)

        print("\n==========================================")
        print("✅ Delete Successful")
        print("==========================================")
        print(f"Deleted: {object_name}")

    except S3Error as error:
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
        print("\n❌ Invalid option. Please choose a number between 1 and 5.")
        print("Returning to main menu...")