def myTheme():
    # Typography
    font = "Lato"
    # At Urban it's the same font for all text but it's good to keep them separate in case you want to change one later.
    labelFont = "Lato" 
    sourceFont = "Lato"
    fontColor = '#4d4d4d'
    # Axes
    axisColor = "#DEDDDD"
    gridColor = "#DEDDDD"
    markColor = "#1696d2"
    backgroundColor = '#ffffff'

    titleFontSize = 20
    subTitleFontSize = 15
    axisTitleFontSize = 12
    textFontSize = 12
    labelFontSize = 10

    # Colors
    main_palette = ["#1696d2", 
                    "#d2d2d2",
                    "#000000", 
                    "#fdbf11", 
                    "#ec008b", 
                    "#55b748", 
                    "#5c5859", 
                    "#db2b27", 
                   ]
    sequential_palette = ["#cfe8f3", 
                          "#a2d4ec", 
                          "#73bfe2", 
                          "#46abdb", 
                          "#1696d2", 
                          "#12719e", 
                         ]
    return {
        # width and height are configured outside the config dict because they are Chart configurations/properties not chart-elements' configurations/properties.
        "config": {
            "title": {
                "fontSize": titleFontSize,
                "font": font,
                "anchor": "start", # equivalent of left-aligned.
                "color": fontColor,
            },
            "guide-title":{
              "color": "Monospace",
              "fontSize": subTitleFontSize,
              "font": labelFont
            },
            "axisX": {
                "domain": True,
                "domainColor": axisColor,
                "domainWidth": 1,
                "grid": False,
                "domainDashOffset": 10,
                "labelFont": labelFont,
                "labelFontSize": labelFontSize,
                "labelAngle": 0, 
                "tickColor": axisColor,
                "titleFont": font,
                "titleFontSize": axisTitleFontSize,
                "titlePadding": 10, # guessing, not specified in styleguide
            },
            "axisY": {
                "domain": False,
                "grid": True,
                "gridColor": gridColor,
                "gridWidth": 1,
                "gridDash":[5,2],
                "domainDashOffset": 10,
                "labelFont": labelFont,
                "labelFontSize": labelFontSize,
                "labelAngle": 0, 
                "titleFont": font,
                "titleFontSize": axisTitleFontSize,
                "titlePadding": 10, # guessing, not specified in styleguide
            },
            "range": {
                "category": main_palette,
                "diverging": sequential_palette,
            },
            "legend": {
                "labelFont": labelFont,
                "labelFontSize": textFontSize,
                "symbolType": "square", # just 'cause
                "symbolSize": 100, # default
                "titleFont": font,
                "titleFontSize": axisTitleFontSize,
                "title": "", # set it to no-title by default
                # "orient": "top-left", # so it's right next to the y-axis
                # "offset": 0, # literally right next to the y-axis.
            },
            "view": {
                'strokeWidth':0, #border around charts. to show, set the border to >0
            },

            ### MARKS CONFIGURATIONS ###
            "area": {
               "fill": markColor,
           },
           "line": {
               "color": markColor,
               "stroke": markColor,
               "strokeWidth": 1,
           },
           "trail": {
               "color": markColor,
               "stroke": markColor
           },
           "path": {
               "stroke": markColor,
           },
           "point": {
               "filled": True,
           },
           "text": {
               "font": sourceFont,
               "color": markColor,
               "fontSize": textFontSize,
               "align": "right",
               "fontWeight": 400,
               "size": 11,
           }, 
           "bar": {
                "fill": markColor,
                "strokeWidth": 0,
            },
        }
    }