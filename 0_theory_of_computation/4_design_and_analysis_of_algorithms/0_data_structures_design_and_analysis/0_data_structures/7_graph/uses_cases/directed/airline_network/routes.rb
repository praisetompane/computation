require('./city.rb')

dallas = City.new("Dallas")
toronto = City.new("Toronto")

dallas.add_route(dallas, 138)
toronto.add_route(dallas, 216)