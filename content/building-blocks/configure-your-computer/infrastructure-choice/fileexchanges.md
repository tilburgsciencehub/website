# Setting Up and Using a File Exchange

[File exchanges](../workflow/directories.md#4-file-exchange) are essential to transfer data *between different stages of your pipeline*, and between *different co-authors* working on a project.

The key requirements of a file exchange are:

- the programmatic access (i.e., via command line tools),
- to data storage organized in directories and files,
- allowing members of the project to upload or download data,
- employing fine-grained access controls (i.e., to give users reading rights, or reading/writing rights).

Below, we show a few options that we've used in our research projects. Please check with your own institution whether the use of these services is permitted.

## Amazon S3

Amazon S3 offers you unlimited storage in so-called "buckets". Think of them as unlimited hard disks. It also offers a platform-independent command line tool (called AWS Command Line Interface, or in short, *AWS CLI*) so that you can write scripts to upload and download data from it.

### Setting up AWS Command Line Interface (AWS CLI)

- Download AWS Command Line Interface [here](https://aws.amazon.com/cli/).
- Make sure it is callable from anywhere on your system, i.e., add the
  installation path to your environment variables (for a recap, see our
  [setup guide](../setup/index.md)).

#### As an administrator of the research project

- Sign up for AWS S3
- Create a "bucket" that will hold the data (name of the bucket, and available region; since we're based in Europe, we choose `eu-central-1` as our location)
- Create a set of user authentication credentials that you can give to your users

All details are [here](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-walkthroughs-managing-access-example1.html).

#### As a user of the research project

- After [downloading and installing AWS CLI](https://aws.amazon.com/cli/), and making sure it is added to your environment variables, open a terminal and type `aws configure`.
- You will be prompted to enter the following details, which you should have
received by the project administrator:

        AWS access key: [paste it here]
        AWS secret access key: [paste it here]
        default region name: eu-central-1 (if you're not located in Europe, choose the corresponding name for your region of the bucket)
        default output format: [just hit enter here; we keep it empty]

- You're all set! You can now use the AWS CLI to download and upload data. Not sure why this is needed? Review our notes on [data management and directory structure](../workflow/directories.md).

### Using the S3 file exchange

- Write scripts that upload and download data from S3, according to your [directory structure and workflows](../workflow/directories.md)
    - For **uploading**, we use the following (platform-independent) command: `aws s3 cp FOLDERNAME s3://BUCKETNAME --recursive --region eu-central-1`

    - For **downloading**, we use the following commands: `aws s3 sync s3://BUCKETNAME TARGETFOLDER`, which downloads the entire contents of `BUCKETNAME` (you can use subdirectories, too!) to the directory `TARGETFOLDER` on your local computer.
    - Sometimes you do want to download only *specific* files rather than entire folders. For example, `aws s3 sync s3://BUCKETNAME/directory1/ TARGETFOLDER --region eu-central-1 --exclude "*" --include "*.json"` downloads only *json* files to the `TARGETFOLDER` on your local computer.

## Dropbox

Raw data files are ideally hosted on a secure server; in practice, many researchers
store their data on Dropbox, though (e.g., because they want to enable
co-authors *not* used to reproducible workflows to also access these
files.

A good way then is to *host* your raw data files in a Dropbox folder. Thereby,
- your co-authors have access to the files (and, e.g., can populate
  the directories with their own data collections)
- you can still programmatically access these files and reproduce
  them to any directory on your hard disk.

Here is a Python script that *downloads* the data to your
local directory structure. In that way, it mimics the "downloading" part of the AWS S3 file exchange described above.

You can upload data simply by moving files to this shared Dropbox folder (yes, just use Dropbox!).

<script src="https://gist.github.com/hannesdatta/10422a6fbb584f245c83361245335741.js"></script>
