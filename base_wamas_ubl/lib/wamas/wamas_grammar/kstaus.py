from collections import OrderedDict

grammar = OrderedDict(
    {
        "Telheader_Quelle": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_source",
        },
        "Telheader_Ziel": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_destination",
        },
        "Telheader_TelSeq": {
            "type": "int",
            "length": 6,
            "dp": False,
            "df_val": False,
            "df_func": "get_sequence_number",
        },
        "Telheader_AnlZeit": {
            "type": "datetime",
            "length": 14,
            "dp": False,
            "df_val": False,
            "df_func": "get_current_datetime",
        },
        "Satzart": {
            "type": "str",
            "length": 9,
            "dp": False,
            "df_val": "KSTAUS050",
            "df_func": False,
        },
        "KstAus_Mand": {
            "type": "str",
            "length": 3,
            "dp": False,
            "dict_key": False,
            "df_val": "000",
            "df_func": False,
        },
        "KstAus_KuNr": {
            "type": "str",
            "length": 13,
            "dp": False,
            "dict_key": "ref",
            "df_val": False,
            "df_func": False,
        },
        "KstAus_ThmId": {
            "type": "str",
            "length": 10,
            "dp": False,
            "dict_key": "wamas_code",
            "df_val": False,
            "df_func": False,
        },
        "KstAus_LagIdKom": {
            "type": "str",
            "length": 6,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "KstAus_RfNr": {
            "type": "int",
            "length": 5,
            "dp": False,
            "dict_key": "priority_sequence",
            "df_val": False,
            "df_func": False,
        },
        "KstAus_SatzKz": {
            "type": "str",
            "length": 1,
            "dp": False,
            "dict_key": "game_identifier",
            "df_val": False,
            "df_func": False,
        },
    }
)
