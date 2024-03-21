import os
import subprocess

def inject_deb_into_ipas(folder_path, deb_file, output_folder):
    folder_path = folder_path.strip().strip('"')
    output_folder = output_folder.strip().strip('"')

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    if not os.path.isdir(output_folder):
        print(f"Error: '{output_folder}' is not a valid directory.")
        return

    ipa_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.ipa')]

    for ipa_file in ipa_files:
        input_path = os.path.join(folder_path, ipa_file)
        output_path = os.path.join(output_folder, f"patched_{ipa_file}")


        input_path_escaped = input_path.replace(" ", r"\ ")
        output_path_escaped = output_path.replace(" ", r"\ ")

        command = f"pyzule -i {input_path_escaped} -o {output_path_escaped} -f {deb_file}"
        subprocess.run(command, shell=True)

    print("Injection completed successfully.")

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing IPA files: ")
    deb_file = input("Enter the path of the DEB file to inject: ")
    output_folder = input("Enter the output folder path: ")

    inject_deb_into_ipas(folder_path, deb_file, output_folder)

