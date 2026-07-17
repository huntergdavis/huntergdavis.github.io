# Hunter Davis .com website - backing data store for jekyll blog

After 20 years this blog has gone through many changes, but I'm really liking the simplicity and low overhead of a jekyll blog

## Local preview on macOS

Install the pinned Homebrew Ruby and the site's gems:

```sh
brew bundle
export PATH="$(brew --prefix ruby@3.3)/bin:$PATH"
bundle config set --local path vendor/bundle
bundle install
```

Start Jekyll with draft/future posts and live reload enabled:

```sh
bundle exec jekyll serve --livereload --future
```

The site will be available at <http://127.0.0.1:4000/>.
