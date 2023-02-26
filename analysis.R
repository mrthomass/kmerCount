read.csv("kmerCount.csv") |>
  ggplot2::ggplot() + ggplot2::geom_line(ggplot2::aes(x = nrep, y = nfound)) +
  ggplot2::theme_bw()

ggplot2::ggsave("readKmers.png", plot = ggplot2::last_plot())
