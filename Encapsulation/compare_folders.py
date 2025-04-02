import os
import filecmp


def compare_folders(folder1, folder2):
    # Perform the directory comparison
    dir_comparison = filecmp.dircmp(folder1, folder2)

    # Compare files that are in both folders and check for differences
    compare_files_in_both_folders(dir_comparison)

    # Recursively compare subdirectories
    for common_dir in dir_comparison.common_dirs:
        print(f"Comparing subfolders: {common_dir}")
        compare_folders(os.path.join(folder1, common_dir), os.path.join(folder2, common_dir))


def compare_files_in_both_folders(dir_comparison):
    # Files only in folder1
    if dir_comparison.left_only:
        print(f"Files only in {dir_comparison.left}:", dir_comparison.left_only)

    # Files only in folder2
    if dir_comparison.right_only:
        print(f"Files only in {dir_comparison.right}:", dir_comparison.right_only)

    # Files with differences in content
    if dir_comparison.diff_files:
        print(f"Files with differences in content:", dir_comparison.diff_files)

        # Compare content of the differing files
        for file in dir_comparison.diff_files:
            file1 = os.path.join(dir_comparison.left, file)
            file2 = os.path.join(dir_comparison.right, file)

            if not filecmp.cmp(file1, file2, shallow=False):
                print(f"  - Content of {file} differs between the two folders")

    # Identical files
    if dir_comparison.same_files:
        print(f"Identical files:", dir_comparison.same_files)


def main():
    # Replace with your folder paths
    folder1 = '/Users/donadab/PycharmProjects/Python advanced/Encapsulation/restaurant/project'
    folder2 = '/Users/donadab/PycharmProjects/Python advanced/Encapsulation/restaurant/project2'

    # Start the comparison
    compare_folders(folder1, folder2)


# Run the main function
if __name__ == "__main__":
    main()
