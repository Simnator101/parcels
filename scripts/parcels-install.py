try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
import os
from datetime import datetime, timedelta
from progressbar import ProgressBar
from argparse import ArgumentParser, RawDescriptionHelpFormatter


class ExampleData(object):

    def __init__(self, url, filenames, path):
        self.url = url
        self.filenames = filenames
        self.path = path

    def download(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        pbar = ProgressBar()
        print("Downloading %s ..." % (self.url.split("/")[-1]))
        for filename in pbar(self.filenames):
            if not os.path.exists(os.path.join(self.path, filename)):
                f = urlopen(self.url + "/" + filename)
                with open(os.path.join(self.path, filename), 'wb') as temp_file:
                    temp_file.write(f.read())

dates = [datetime(2002, 1, 1) + timedelta(days=x) for x in range(0, 365)]
globfiles = [x.strftime("%Y%m%d") + "000000-GLOBCURRENT-L4-CUReul_hs-ALT_SUM-v02.0-fv01.0.nc"
             for x in dates]
example_data = [
    ExampleData(url="http://oceanparcels.org/examples-data/MovingEddies_data",
                filenames=["moving_eddiesP.nc", "moving_eddiesU.nc", "moving_eddiesV.nc"],
                path="examples/MovingEddies_data"),
    ExampleData(url="http://oceanparcels.org/examples-data/OFAM_example_data",
                filenames=["OFAM_simple_U.nc", "OFAM_simple_V.nc"],
                path="examples/OFAM_example_data"),
    ExampleData(url="http://oceanparcels.org/examples-data/Peninsula_data",
                filenames=["peninsulaU.nc", "peninsulaV.nc", "peninsulaP.nc"],
                path="examples/Peninsula_data"),
    ExampleData(url="http://oceanparcels.org/examples-data/GlobCurrent_example_data",
                filenames=globfiles, path="examples/GlobCurrent_example_data"),
    ExampleData(url="http://oceanparcels.org/examples-data/DecayingMovingEddy_data",
                filenames=["decaying_moving_eddyU.nc", "decaying_moving_eddyV.nc"],
                path="examples/DecayingMovingEddy_data")
]


if __name__ == "__main__":

    parser = ArgumentParser(description="""Install Parcels and its examples.""",
                            epilog="""
The install process attempts to build a complete environment equipped to
run all features and tutorials contained in Parcels. This includes
downloading examples data and can therefore take a few minutes.
""",
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("--download-examples", action="store_true", default=True,
                        help="Download hydrodynamic data required to run examples")

    args = parser.parse_args()

    # Download example files
    if args.download_examples:
        for data in example_data:
            data.download()
