Help me plan building a stream lit dashboard for my options trading. I have prototyped some matplotlib plots in the trade_lab. The charts that we want to focus on:
- GEX Price (this is over 10 calendar days) - this includes the zero gamma line and spot
- GEX Strike (this is over 10 calendar days)
- SPX 5 min candles (Candles chart)
- DirectionalGammaImbalance
- GrossGEX
- StrikeGammaSingleExp

And then secondarily I'd like to have something on volume and open interest. Using one ore more of the charts:
- OpenInterestComparison
- VolumeByExpiry
- VolumeDelta

You can find examples of how to use these charts in the following notebooks. The actual charts are located in the /repos/trade_lab/src/trade_lab/charts folder. For simplicity, let's just copy over the charts we want to use to the options_dashboard/src/charts folder. We'll consolidate later.

I think we should break the dashboard up into separate tabs. One for managing today's trade and one for assessing new trades.

Managing trades tab should include GEX Price which helps assess teh market regime, SPX 5 min candles, DirectionalGammaImbalance, GrossGEX, and maybe the StrikeGammaSingleExp for today's option chain. This tab should just default to showing the today's data, but it should be parameterized by the ticker symbol.

The assessing trade tab should include GEX Strike (this is over 10 calendar days). This tab should be parameterized both by the expiration date and the ticker symbol.

Let's default the ticker symbol to SPXW since that's what I'm trading mostly.

All the data is located in a folder specified by the DATA_DEV env variable.

Finally, we want to add a collapsable chat on the right hand side of the dashboard that we will eventually hook up to an agent.

We'll also need to setup some sort of routine to regularly pull the data and refresh the dashboard. Currently some scripts in the trade_lab/bin folder are what pull the data from schwab. We will need to setup like a routine that runs every 5 minutes to refresh the data. Let's actually ignore this until we have the dashboard setup and then we'll comback to it.

Some questions:
- what's the best way to display these charts? What order is most useful when trading?
- what other data or metrics would be helpful to display?

Does this make sense? What other considerations are there? Help me break this down into discrete tasks. Let's create a file in the docs folder with the plan.