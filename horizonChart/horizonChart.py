import altair as alt
import pandas as pd
import numpy as np


class HorizonChartGenerator(object):
    def __init__(self, data: pd.DataFrame, X: str, Y: str, noLevels):
        self.data = data
        self.X = X
        self.Y = Y
        self.noLevels = noLevels
        self.domain = self._setDomain()
        self.offset = self._setOffset()

        self._transform()

        self.chart = None

    def _setDomain(self):
        lower = 0
        upper = np.max(np.absolute(self.data[self.Y]))
        self.domain = [lower, ((upper-lower)/self.noLevels)]
        return self.domain

    def _setNegative(self):
        self.data['negative'] = self.data[self.Y].apply(lambda x: x < 0)

    def _setLevels(self):
        for i in range(0, self.noLevels+1):
            self.data['pos_level' +
                      str(i)] = self.data[self.Y].apply(lambda x: x-self.offset*i)
            self.data['neg_level' +
                      str(i)] = self.data[self.Y].apply(lambda x: -x-self.offset*i)

    def _setOffset(self):
        self.offset = self.domain[1]
        return self.offset

    def _transform(self):
        self._setNegative()
        self._setLevels()

    def _getLayer(self, y, color='blue'):
        base = alt.Chart(self.data).mark_area(
            clip=True,
            opacity=0.3,
            color=color
        ).encode(
            alt.X(
                self.X,
                axis=alt.Axis(labels=False, grid=False, ticks=False),
                scale=alt.Scale(zero=False, nice=False)),
            alt.Y(
                y, 
                scale=alt.Scale(domain=self.domain),
                axis=alt.Axis(labels=False, grid=False, ticks=False),
                title=None
                ),
        )
        return base

    def generate(self):
        layers = []
        for i in range(0, self.noLevels):
            layers = layers + [
                self._getLayer(
                    y=('pos_level'+str(i)),
                    color='blue'),
                self._getLayer(
                    y=('neg_level'+str(i)),
                    color='red')
                ]
        self.chart = alt.layer(*layers)
        return self.chart
