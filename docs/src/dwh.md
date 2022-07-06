Module src.dwh
==============

Classes
-------

`Features(**kwargs)`
:   This class defines the metadata for the table generated for features.
    
    A simple constructor that allows initialization from kwargs.
    
    Sets attributes on the constructed instance using the names and
    values in ``kwargs``.
    
    Only keys that are present as
    attributes of the instance's class are allowed. These could be,
    for example, any mapped columns or relationships.

    ### Ancestors (in MRO)

    * sqlalchemy.orm.decl_api.Base

    ### Instance variables

    `catfeat`
    :

    `id`
    :

    `name`
    :

    `numfeat`
    :

    `targfeat`
    :

`PredResults(**kwargs)`
:   This class defines the metadata for the table generated to store the results of the predictions
    
    A simple constructor that allows initialization from kwargs.
    
    Sets attributes on the constructed instance using the names and
    values in ``kwargs``.
    
    Only keys that are present as
    attributes of the instance's class are allowed. These could be,
    for example, any mapped columns or relationships.

    ### Ancestors (in MRO)

    * sqlalchemy.orm.decl_api.Base

    ### Instance variables

    `MAE`
    :

    `MAPE`
    :

    `MSE`
    :

    `Model`
    :

    `R2`
    :

    `RMSE`
    :

    `RMSLE`
    :

    `date_created`
    :

    `id`
    :

    `index`
    :

    `time_in_seconds`
    :