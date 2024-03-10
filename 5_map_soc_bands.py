import pandas as pd
import rasterio as rio
import os

SCENE_PATH = "sat"
SOURCE_PATH = "IL-BR.csv"
FINAL_CSV = "final.csv"
BANDS = ["B01",
         "B02",
         "B03",
         "B04",
         "B05",
         "B06",
         "B07",
         "B8A",
         "B08",
         "B09",
         "B11",
         "B12"
         ]


def find_tiff(band):
    for tiff in os.listdir(SCENE_PATH):
        if band in tiff:
            return tiff
    return None


def get_soc_rows():
    df = pd.read_csv(SOURCE_PATH)
    coordinates = []
    for index, row in df.iterrows():
        point_id = row["location_id"]
        oc = row["SOCc"]
        lon = row["X"]
        lat = row["Y"]
        coordinates.append((point_id, lon, lat, oc))
    return coordinates


def get_band_values(band):
    print(f"Processing {band}")
    tiff = find_tiff(band)
    tiff_path = os.path.join(SCENE_PATH, tiff)
    soc_rows = get_soc_rows()
    pixels = []
    with rio.open(tiff_path) as src:
        for point_id, lon, lat, oc in soc_rows:
            row, col = src.index(lon, lat)
            pixel_value = src.read(1, window=((row, row + 1), (col, col + 1)))
            if pixel_value.shape[0] != 0 and pixel_value.shape[1] != 0:
                pixels.append([point_id, oc, pixel_value[0][0]])
    return pixels


def merge_bands(all_bands_pixels_df, band, band_pixels):
    band_df = pd.DataFrame(band_pixels, columns=["location_id","SOCc",band])
    if all_bands_pixels_df is None:
        return band_df
    band_df = band_df[["location_id",band]]
    all_bands_pixels_df = pd.merge(all_bands_pixels_df, band_df, on="location_id")
    return all_bands_pixels_df


def process_scene():
    all_bands_pixels_df = None
    for band in BANDS:
        band_pixels = get_band_values(band)
        all_bands_pixels_df = merge_bands(all_bands_pixels_df, band, band_pixels)

    #all_bands_pixels_df = sanitize(all_bands_pixels_df)
    all_bands_pixels_df.to_csv(FINAL_CSV, index=False)


def sanitize(df):
    df = df[
            (df["B01"]!=0)
        |   (df["B02"]!=0)
        |   (df["B03"]!=0)
        |   (df["B04"]!=0)
        |   (df["B05"]!=0)
        |   (df["B06"]!=0)
        |   (df["B07"]!=0)
        |   (df["B8A"]!=0)
        |   (df["B08"]!=0)
        |   (df["B09"]!=0)
        |   (df["B11"]!=0)
        |   (df["B12"]!=0)
         ]
    return df


if __name__ == "__main__":
    process_scene()