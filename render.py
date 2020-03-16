from cvkeskus_parser import cvkeskus_parse
from cvonline_parser import cvonline_parse
from combine import combine

import json

from staticjinja import Site


def render():
    if __name__ == "__main__":
        with open('data.json', 'r', encoding="utf8") as file:
            context = {
                'offers': json.loads(file.read()),
            }

        site = Site.make_site(env_globals=context)

        site.render(use_reloader=True)


cvkeskus_parse()
cvonline_parse()
combine()
render()
