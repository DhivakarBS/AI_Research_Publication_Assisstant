function Navbar() {
  return (
    <nav className="border-b border-slate-800 bg-slate-950/80 backdrop-blur">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <div>
          <p className="text-xl font-semibold">ResearchAI</p>
          <p className="text-sm text-slate-400">IEEE Compliance Engine</p>
        </div>
        <div className="flex gap-6 text-sm text-slate-300">
          <a href="#" className="hover:text-cyan-400">Home</a>
          <a href="#" className="hover:text-cyan-400">Dashboard</a>
          <a href="#" className="hover:text-cyan-400">Docs</a>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
