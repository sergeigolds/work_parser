import json

from staticjinja import Site

if __name__ == "__main__":
    with open('output.json', 'r', encoding="utf8") as file:
        context = {
            'offers': json.loads(file.read()),
        }

    site = Site.make_site(env_globals=context)

    site.render(use_reloader=True)
