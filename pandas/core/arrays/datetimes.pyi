import numpy as np
#from pandas._libs import lib as lib, tslib as tslib
#from pandas._libs.tslibs import NaT as NaT, conversion as conversion, iNaT as iNaT, normalize_date as normalize_date
#from pandas._libs.tslibs import Timestamp as Timestamp #, ccalendar as ccalendar, fields as fields, timezones as timezones, tzconversion as tzconversion
#from pandas.core.algorithms import checked_add_with_arr as checked_add_with_arr
from pandas.core.arrays import datetimelike as dtl
#from pandas.core.arrays._ranges import generate_regular_range as generate_regular_range
#from pandas.core.dtypes.common import is_categorical_dtype as is_categorical_dtype, is_datetime64_any_dtype as is_datetime64_any_dtype, is_datetime64_dtype as is_datetime64_dtype, is_datetime64_ns_dtype as is_datetime64_ns_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_float_dtype as is_float_dtype, is_object_dtype as is_object_dtype, is_period_dtype as is_period_dtype, is_string_dtype as is_string_dtype, is_timedelta64_dtype as is_timedelta64_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype
#from pandas.core.dtypes.generic import ABCIndexClass as ABCIndexClass, ABCPandasArray as ABCPandasArray, ABCSeries as ABCSeries
#from pandas.core.dtypes.missing import isna as isna
#from pandas.errors import PerformanceWarning as PerformanceWarning
#from pandas.tseries.frequencies import get_period_alias as get_period_alias, to_offset as to_offset
#from pandas.tseries.offsets import Day as Day, Tick as Tick
from typing import Any, Optional, Union

def tz_to_dtype(tz: Any): ...

class DatetimeArray(dtl.DatetimeLikeArrayMixin, dtl.TimelikeOps, dtl.DatelikeOps):
    __array_priority__: int = ...
    def __init__(self, values: Any, dtype: Any = ..., freq: Optional[Any] = ..., copy: bool = ...) -> None: ...
    @property
    def dtype(self) -> Union[np.dtype, DatetimeTZDtype]: ...
    @property
    def tz(self): ...
    @tz.setter
    def tz(self, value: Any) -> None: ...
    @property
    def tzinfo(self): ...
    @property
    def is_normalized(self): ...
    def __array__(self, dtype: Any=...) -> np.ndarray: ...
    def __iter__(self) -> Any: ...
    def astype(self, dtype: Any, copy: bool = ...): ...
    def tz_convert(self, tz: Any): ...
    def tz_localize(self, tz: Any, ambiguous: str = ..., nonexistent: str = ...): ...
    def to_pydatetime(self): ...
    def normalize(self): ...
    def to_period(self, freq: Optional[Any] = ...): ...
    def to_perioddelta(self, freq: Any): ...
    def month_name(self, locale: Optional[Any] = ...): ...
    def day_name(self, locale: Optional[Any] = ...): ...
    @property
    def time(self): ...
    @property
    def timetz(self): ...
    @property
    def date(self): ...
    year: Any = ...
    month: Any = ...
    day: Any = ...
    hour: Any = ...
    minute: Any = ...
    second: Any = ...
    microsecond: Any = ...
    nanosecond: Any = ...
    weekofyear: Any = ...
    week: Any = ...
    dayofweek: Any = ...
    weekday: Any = ...
    dayofyear: Any = ...
    quarter: Any = ...
    days_in_month: Any = ...
    daysinmonth: Any = ...
    is_month_start: Any = ...
    is_month_end: Any = ...
    is_quarter_start: Any = ...
    is_quarter_end: Any = ...
    is_year_start: Any = ...
    is_year_end: Any = ...
    is_leap_year: Any = ...
    def to_julian_date(self): ...

def sequence_to_dt64ns(data: Any, dtype: Optional[Any] = ..., copy: bool = ..., tz: Optional[Any] = ..., dayfirst: bool = ..., yearfirst: bool = ..., ambiguous: str = ...): ...
def objects_to_datetime64ns(data: Any, dayfirst: Any, yearfirst: Any, utc: bool = ..., errors: str = ..., require_iso8601: bool = ..., allow_object: bool = ...): ...
def maybe_convert_dtype(data: Any, copy: Any): ...
def maybe_infer_tz(tz: Any, inferred_tz: Any): ...
def validate_tz_from_dtype(dtype: Any, tz: Any): ...
