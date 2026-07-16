import Navbar from './components/Navbar';
import Footer from './components/Footer';

function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <Navbar />
      <main className="mx-auto flex max-w-6xl flex-col gap-8 px-6 py-16">
        <section className="rounded-2xl border border-slate-800 bg-slate-900/70 p-10 shadow-2xl">
          <p className="mb-4 text-sm uppercase tracking-[0.3em] text-cyan-400">Sprint 1</p>
          <h1 className="text-4xl font-semibold">ResearchAI Platform Foundation</h1>
          <p className="mt-4 max-w-2xl text-lg text-slate-300">
            A scalable architecture for the IEEE compliance workflow with a clean backend,
            structured configuration, and a polished frontend shell.
          </p>
        </section>
        <section className="grid gap-6 md:grid-cols-3">
          <div className="rounded-xl border border-slate-800 bg-slate-900/70 p-6">
            <h2 className="text-xl font-semibold">Backend Ready</h2>
            <p className="mt-2 text-slate-300">FastAPI, SQLAlchemy, Alembic, and logging are scaffolded.</p>
          </div>
          <div className="rounded-xl border border-slate-800 bg-slate-900/70 p-6">
            <h2 className="text-xl font-semibold">Frontend Shell</h2>
            <p className="mt-2 text-slate-300">React, Vite, Tailwind, and a dashboard placeholder are prepared.</p>
          </div>
          <div className="rounded-xl border border-slate-800 bg-slate-900/70 p-6">
            <h2 className="text-xl font-semibold">Architecture First</h2>
            <p className="mt-2 text-slate-300">The sprint intentionally avoids validation and AI implementation.</p>
          </div>
        </section>
      </main>
      <Footer />
    </div>
  );
}

export default App;
