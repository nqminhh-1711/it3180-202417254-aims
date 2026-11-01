# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-11-02
### Added
- Cart.sort_by_title() and Cart.sort_by_cost() to sort items in cart.
- search_by_category() in aims.search to search DVDs by category.

## [1.0.0] - 2026-11-01
### Added
- Cart.print_cart() for displaying ordered items and total cost.
- search_by_title() in aims.search for keyword-based DVD search.
- Cart.total_cost_with_discount() to calculate discounted cart total.
- Automated unit testing with unittest discover.
- Pull request template and documentation.

### Fixed
- Reject DVDs beyond MAX_NUMBERS_ORDERED (20) in cart (#7).
- Validate discount percent range between 0 and 100 in total_cost_with_discount.
