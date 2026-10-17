# Simulate Serverless Cold Start Delay

This example demonstrates the 'cold start' phenomenon often encountered with serverless functions or free-tier hosting. It runs a simple Python HTTP server that introduces a significant delay on the first request after a period of inactivity, simulating the time it takes for an environment to spin up. Subsequent requests within the inactivity threshold will be served much faster, illustrating the difference between cold and warm starts.

## Language

`python`

## How to Run

1. Save the code as `main.py`.
2. Run the script from your terminal: `python main.py`.
3. Open your web browser to `http://localhost:8000/` or use `curl http://localhost:8000/`. Observe the initial delay, then refresh quickly to see faster responses. Wait for more than 10 seconds and refresh again to trigger another cold start.

## Original Article

This example accompanies the Turkish article: [Ücretsiz Sunucularla İnceleme Botunuzu Kullanmadan Önce Soğuk Başlangıcı (Cold Start) Göz Ardı Etmeyin](https://fatihsoysal.com/blog/ucretsiz-sunucularla-inceleme-botunuzu-kullanmadan-once-soguk-baslangici-cold-start-goz-ardi-etmeyin/).

## License

MIT — see [LICENSE](LICENSE).
