#from pandas import DataFrame as DataFrame
#from pandas.core.dtypes.common import is_bool_dtype as is_bool_dtype, is_categorical_dtype as is_categorical_dtype, is_datetime64_dtype as is_datetime64_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_integer_dtype as is_integer_dtype, is_numeric_dtype as is_numeric_dtype, is_period_dtype as is_period_dtype, is_string_dtype as is_string_dtype, is_timedelta64_dtype as is_timedelta64_dtype
#from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype
from typing import Any, Optional

loads: Any

def as_json_table_type(x: Any): ...
def set_default_names(data: Any): ...
def convert_pandas_type_to_json_field(arr: Any, dtype: Optional[Any] = ...): ...
def convert_json_field_to_pandas_type(field: Any): ...
def build_table_schema(data: Any, index: bool = ..., primary_key: Optional[Any] = ..., version: bool = ...): ...
def parse_table_schema(json: Any, precise_float: Any): ...