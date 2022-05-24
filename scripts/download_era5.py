import src.download as download

# download geopotential at 500 hPa
download.main(
    mode='separate',
    variable=['geopotential'],
    level_type='pressure',
    pressure_level=['500'],   
    output_dir='/home/steidani/windows/data/ParetoBoost/z500/',
    years=download.all_years,
    month=download.all_months,
    day=download.all_days,
    time=download.all_times,
    resolution=download.resolution

)

# download 2m temperature (single level)
download.main(
    mode='separate',
    variable=['2m_temperature'],
    level_type='single',  
    output_dir='/home/steidani/windows/data/ParetoBoost/t2m/',
    years=download.all_years,
    month=download.all_months,
    day=download.all_days,
    time=download.all_times,
    resolution=download.resolution
)

# download constant variables
download.main(
    mode='separate',
    variable=['orography', 'land_sea_mask'],
    level_type='single',  
    output_dir='/home/steidani/windows/data/ParetoBoost/constants/',
    years=['1979'],
    month=['01'],
    day=['01'],
    time=['00:00'],
    resolution=download.resolution,
    custom_fn='constants_1.875.nc'
)