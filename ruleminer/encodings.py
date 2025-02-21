"""Encoding definitions
"""

encodings_definitions = {
    "percentage": 'def percentage(c):\n\
    if not isinstance(c, pd.Series):\n\
        return ["100%" if i == 1 else\n\
                "50%"  if i == 0.5 else\n\
                "0%"   if i == 0 else\n\
                "<50%"  if i < 0.5 and i != 0 else\n\
                ">50%"  if i > 0.5 and i != 1 else "unknown" for i in c]\n\
    else:\n\
        return pd.Series(index = c.index, data = ["100%" if i == 1 else\n\
                "50%"  if i == 0.5 else\n\
                "0%"   if i == 0 else\n\
                "<50%"  if i < 0.5 and i != 0 else\n\
                ">50%"  if i > 0.5 and i != 1 else "unknown" for i in c])',
    "reported": 'def reported(c):\n\
    if not isinstance(c, pd.Series):\n\
        if isinstance(c, list):\n\
            return ["not reported" if np.isnan(i) else "not reported" if i == 0 else "reported" for i in c]\n\
        else:\n\
            return "not reported" if np.isnan(c) else "not reported" if c == 0 else "reported"\n\
    else:\n\
        return pd.Series(index = c.index, data = ["not reported" if np.isnan(i) else "not reported" if i == 0 else "reported" for i in c])',
    "nonreported": 'def nonreported(c):\n\
    return ["not reported" if pd.isna(i) else str(i) for i in c]',
    "EEA_country": "def EEA_country(c):\n\
    return pd.Series(index = c.index, data = ['EEA' if (i in ['AUSTRIA','BELGIUM','BULGARIA','CROATIA','CYPRUS','CZECH REPUBLIC','CZECHIA','DENMARK','ESTONIA','FINLAND',\
'FRANCE','GERMANY','GREECE','HUNGARY','ICELAND','IRELAND','ITALY','LATVIA','LIECHTENSTEIN','LITHUANIA','LUXEMBOURG','MALTA','NETHERLANDS','NORWAY',\
'POLAND','PORTUGAL','ROMANIA','SLOVAKIA','SPAIN','SWEDEN','SWITZERLAND','UNITED KINGDOM']) else 'non-EEA' for i in c])",
}
