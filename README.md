# Entertainment Center

Entertainment Center builds a static webpage using information obtained from
IMDb's Top 250 and youtube. The generated website displays the movie title 
and poster image. Clicking on the poster image will play a video that 
represents the first result returned from a youtube search using the search 
term `{movie title} official trailer`.     

## Prerequisites

*   Python 2.7.14 or greater
*   The pip package management tool
*   The Google APIs Client Library for Python >= 1.6.4:
    ```
    pip install --upgrade google-api-python-client
    ```
*   The IMDbPY Library for Python >= 5.2:
    ```bash
    curl -L -O https://github.com/alberanid/imdbpy/archive/master.zip
    unzip master.zip        
    cd imdbpy-master/
    python ./setup.py --without-sqlobject --without-sqlalchemy install
    ```    

## Usage

```
usage: entertainment_center.py [-h] -k KEY [-M MAX_RESULTS]

optional arguments:
  -h, --help                                    show this help message and exit
  -k KEY, --key KEY                             Google API developer key
  -M MAX_RESULTS, --max-results MAX_RESULTS     Max results

```
### References

* [IMDbPY](https://imdbpy.sourceforge.io/downloads.html)
* [google/google-api-python-client](https://github.com/google/google-api-python-client)
* [Youtube API Search Sample](https://github.com/youtube/api-samples/blob/master/python/search.py)
* [Google Cloud Platform](https://console.cloud.google.com/)

## License 

Entertainment Center is distributed under the MIT license.