require 'liquid'
require 'uri'

# https://stackoverflow.com/a/23453152/17082981
# Capitalize all words of the input
module Jekyll
  module CapitalizeAll
    def capitalize_all(words)
      return words.split(' ').map(&:capitalize).join(' ')
    end
  end
end

Liquid::Template.register_filter(Jekyll::CapitalizeAll)