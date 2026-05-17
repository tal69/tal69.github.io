source "https://rubygems.org"

# Modern Jekyll (4.x). We build the site ourselves locally and via GitHub
# Actions — we do NOT use the github-pages gem, because it pins Jekyll to 3.9
# and Liquid 4.0, which don't run on Ruby 3.4+ (uses removed `tainted?` etc.).
gem "jekyll", "~> 4.4"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.17"
  gem "jekyll-seo-tag", "~> 2.8"
  gem "jekyll-sass-converter", "~> 3.0"
end

# Required on macOS / newer Ruby (3.4+ / 4.0+ removed these from the default
# standard library, so they must be declared explicitly).
gem "webrick", "~> 1.8"
gem "bigdecimal"
gem "csv"
gem "logger"
gem "base64"
gem "mutex_m"
gem "ostruct"
gem "drb"
gem "fiddle"
