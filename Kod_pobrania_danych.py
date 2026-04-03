import cdsapi

c = cdsapi.Client(url="https://cds.climate.copernicus.eu/api", 
                  key="YOUR_ACTUAL_KEY_HERE")

variables = [
    '2m_temperature',
    '2m_dewpoint_temperature',
    'total_precipitation',
    'surface_solar_radiation_downwards',
    'surface_thermal_radiation_downwards',
    '10m_u_component_of_wind',
    '10m_v_component_of_wind',
    'surface_pressure'
]

for year in range(1994, 2024):  # 30 lat
    print(f"Pobieram {year} ...")

    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'format': 'netcdf',
            'product_type': 'reanalysis',

            'variable': variables,
            'year': str(year),
            'month': [f"{m:02d}" for m in range(1, 13)],
            'day': [f"{d:02d}" for d in range(1, 32)],

            # wartość dziennie 
            'time': ['12:00'],

            # Barcelona bbox
            'area': [41.6, 2.0, 41.1, 2.4],
        },
        f'barcelona_era5_daily_{year}.nc'
    )

    print(f"✔ {year} pobrany.")
