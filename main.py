#!python3
import argparse
import os

from github import Github, MainClass


if __name__ == '__main__' :
    parser = argparse.ArgumentParser()

    parser.add_argument("--token", "-t", action="store", type=str, default=None, help="Github token or login.")
    parser.add_argument("--password", "-p", action="store", type=str,  default=None, help="Github token password or password.")
    parser.add_argument("--github-url", action="store", type=str, default=MainClass.DEFAULT_BASE_URL, help="Github URL. Github.com as default.")
    parser.add_argument("--user", type=str, default=None, help="Github user from which to get repos. Cannot be used along with --org")
    parser.add_argument("--org", type=str, default=None , help="Github organisation from which to get repos. Cannot be used along with --user")

    args = parser.parse_args()

    if not bool(args.user) ^ bool(args.org) : # XOR opperator
        print("Please use one of --user and --org !")
        exit(1)

    g = Github(login_or_token=args.token, password=args.password, base_url=args.github_url)

    repos = g.get_user(args.user).get_repos() if args.user else g.get_organization(args.org).get_repos()

    for repo in repos:
        print(repo)
        print(repo.url)
