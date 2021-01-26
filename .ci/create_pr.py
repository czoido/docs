import argparse
import os

from github import Github

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Release to github')
    parser.add_argument('--repo', help='conan-io/docs', required=True)
    parser.add_argument('--head',
                        help='Branch you want to merge',
                        required=True)
    parser.add_argument('--base', help='Branch to merge to', required=True)
    args = parser.parse_args()
    print("Create a PR to {}, to merge {} in {}".format(
        args.repo, args.head, args.base))
    GH_TOKEN = os.getenv("GH_TOKEN")
    gh = Github(GH_TOKEN)
    repo = gh.get_repo(args.repo)
    pr = repo.create_pull(
        title="[ci-bot] Updating {} to merge changes in {}".format(
            args.base, args.head),
        body="",
        head=args.head,
        base=args.base)
