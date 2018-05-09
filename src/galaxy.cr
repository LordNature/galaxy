require "kemal"
require "./galaxy/*"

module Galaxy
  get "/" do
    view(home)
  end
end

Kemal.run
