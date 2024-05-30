# https://github.com/inukshuk/jekyll-scholar/blob/main/lib/jekyll/scholar/plugins/smallcaps.rb
module Jekyll
    class Smallcaps
        def apply(words)
          # Use of \g<1> pattern back-reference to allow for capturing nested {} groups.
          # The first (outermost) capture of $1 is used.
          words.to_s.gsub(/\\textsc(\{(?:[^{}]|\g<1>)*\})/) {
            "<font style=\"font-variant: small-caps\">#{$1[1..-2]}</font>"
          }
        end
    end
end