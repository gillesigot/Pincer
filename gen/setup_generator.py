from os import walk


def get_packages():
    return '\n\t'.join(
        item[0].replace("./", "").replace("\\", ".").replace("/", ".")
        for item in list(walk('pincer')) if "__pycache__" not in item[0]
    )


def get_requires():
    with open("requirements.txt") as f:
        return '\n\t'.join(f.read().strip().splitlines())


def get_testing_requires():
    with open("requirements_dev.txt") as f:
        return '\n\t'.join(f.read().strip().splitlines())


def get_version():
    with open("pincer/__init__.py") as f:
        init_file = f.read().strip().splitlines()

    for line in init_file:
        if line.startswith('__version__'):
            return line[15:-1].replace('-dev', '')


def main():
    version = get_version()

    with open("VERSION", "w") as f:
        f.write(version)

    packages = get_packages()

    with open("gen/setup_base.cfg") as f:
        base = f.read()

    requires = get_requires()
    testing_requires = get_testing_requires()

    with open("setup.cfg", "w") as f:
        f.write(
            base.format(
                version=version,
                packages=packages,
                requires=requires,
                testing_requires=testing_requires
            )
        )


if __name__ == '__main__':
    main()
