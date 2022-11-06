# All dates must be in the yyyy-mm-dd format
SERIES_START_DATE = "2019-01-01"
CHART_START_DATE = "2020-01-01"
LAST_FOCUS_SURVEY = "2022-10-28"
BACEN_API_ADDRESS = f"https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativaMercadoMensais?%24format=json&%24filter=Indicador%20eq%20'IPCA'%20and%20Data%20eq%20'{LAST_FOCUS_SURVEY}'%20and%20baseCalculo%20eq%201"

x_axis_config = {
    'num_font': {'name': 'Calibri', 'size': 12},
    'date_axis': True,
    'num_format': 'mmm-yy',
    'label_position': 'low',
    'major_unit': 1,
    'major_unit_type': 'years'
}

y_axis_config = {
    'num_font': {'name': 'Calibri', 'size': 12},
    'min': -1.1,
    'max': 1.9,
    'major_unit': 0.5,
    'major_gridlines': {'visible': False}
}

y2_axis_config = {
    'num_font': {'name': 'Calibri', 'size': 12},
    'min': -4,
    'max': 14,
    'major_unit': 2,
}

legend_config = {
    'position': 'bottom',
    'font': {'name': 'Calibri', 'size': 12}
}