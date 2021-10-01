import typer

from ssg.site import site


def main(source="content", dest="dlist"):
    config = {"source": source, "dest": dest}

    Site(**config).build()

typer.run(main)
