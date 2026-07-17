# encoding: utf-8
import re

with open('index.html', 'r', encoding='utf-8') as f:
    data = f.read()

old = 'GameNN Architecture Evolution: From Game Simulation to Intelligent Decision'
new = 'GameNN 架构演化：从博弈推演到通用智能决策'
data = data.replace(old, new)

old = 'XuanMu Security Team — @guaidao2'
new = '玄幕安全团队 — @guaidao2'
data = data.replace(old, new)

old = 'July 2026'
new = '2026 年 7 月'
data = data.replace(old, new)

old = '4 Repos · 5 Generations'
new = '5 代演化 · 4 个独立仓库'
data = data.replace(old, new)

old = 'Game-Theoretic Decision'
new = '博弈决策架构'
data = data.replace(old, new)

old = 'Hierarchical RL'
new = '分层强化学习'
data = data.replace(old, new)

old = 'World Model'
new = '世界模型'
data = data.replace(old, new)

old = 'Sidecar Architecture'
new = '侧枝架构'
data = data.replace(old, new)

# Replace the abstract paragraph
old_abstract = '''<strong>Abstract:</strong> This paper systematically traces the complete evolution of the GameNN family.
        GameNN originated as a 16-node network attack-defense simulation engine (Game-nn Simulator)
        combining hierarchical mixture-of-experts routing with a full RSSM world model,
        trained via PPO+GAE self-play.
        It evolved into Game-nn-O, a dual-path architecture fusing a MiniMind language model
        with the Game-NN decision core for structured game-theoretic reasoning.
        The third generation extracted a domain-agnostic decision backbone —
        GameNN World Model — defining five composable modules:
        StateEncoder, RNNDecisionStep, ActionValueHead, WorldModelStep, and Fuser.
        The fourth generation, MuLun-Mind, embedded GameNN as a sidecar decision module
        for language models via ThinkFuser, reusing lm_head.weight at zero extra parameter cost.
        The fifth generation, MuLun-Waf, stripped the LLM backbone entirely,
        keeping only the 65K-parameter sidecar network with a cascaded rule + ML architecture
        and an active learning loop for continuous evolution.
        Recent validation in Tank Chess (a turn-based tactical board game) shows
        GameNN achieving 73% win rate with only 54K parameters,
        outperforming expert rule-based systems and validating the architecture's
        general decision-making capability.'''

new_abstract = '''<strong>摘要：</strong>本文系统梳理 GameNN 系列的完整演化路径与核心设计思想。
        GameNN 起源于一个 16 节点网络攻防推演引擎（Game-nn Simulator），
        采用分层混合专家路由（TreeRouter + Gumbel-Softmax）与完整 RSSM 世界模型，
        以 PPO+GAE 自博弈训练，支持红蓝双方共用权重交替训练。
        随后演化为 Game-nn-O 双路径架构，将 MiniMind 语言模型与 Game-NN 决策核心融合，
        实现"自然语言理解 → 结构化状态 → 博弈推理 → 世界模型预测 → 反思输出"的完整链路。
        第三阶段提取出领域无关的通用决策底座 GameNN World Model，
        定义五个可组合模块：StateEncoder、RNNDecisionStep（GRU 门控）、
        ActionValueHead（策略/动作/价值三头）、WorldModelStep、Fuser。
        该架构的关键设计理念是"本能 + 策略覆盖"——攻击是本能（持续索敌/转向/开火），
        策略层（aggressive / balanced / defensive）决定何时打断本能去执行撤退、补给等动作。
        第四阶段由 MuLun-Mind 将 GameNN 作为侧枝决策模块嵌入语言模型，
        通过 ThinkFuser 零额外参数复用 lm_head.weight 将决策偏置注入 LM logits，
        仅在 &lt;think&gt; token 位置激活，计算量从 O(T) 降至 O(K)（K &lt;&lt; T）。
        第五阶段 MuLun-Waf 彻底剥离 LLM 骨干，仅保留 65K 参数侧枝决策网络，
        以 33 条静态规则（L1）+ ML 模型（L2）+ 置信度门控（L3）级联检测架构，
        配合主动学习循环实现持续进化，CPU 单核推理延迟 &lt; 50μs。'''

data = data.replace(old_abstract, new_abstract)

# Add new paragraphs after the abstract
old_keywords = '''<div class="keywords">
        <span class="kw">博弈决策架构</span>
        <span class="kw">分层强化学习</span>
        <span class="kw">世界模型</span>
        <span class="kw">侧枝架构</span>
        <span class="kw">RSSM</span>
        <span class="kw">MuLun 幕论</span>
        <span class="kw">Gumbel-Softmax</span>
        <span class="kw">Tank Chess</span>
        <span class="kw">LLM 幻觉抑制</span>
      </div>'''

new_section = '''<strong>最新验证：</strong>在回合制策略游戏 Tank Chess（10x10 棋盘，8 坦克混战）中，
        以仅 54K 参数的 GameNN-S16 参赛，在 20 局比赛中取得 73% 胜率（GameNN-S64 更是达到 11 胜），
        远超专家规则系统 RuleBased（3 胜）。验证了三个关键结论：
        (1) 54K 参数足以在策略游戏中超越手写规则 AI；
        (2) GRU 门控状态在回合制决策中比 MLP 有显著优势；
        (3) 分层策略头 + 本能覆盖架构是有效的通用设计范式。
        Transformer 也已作为参赛者加入，在监督学习阶段损失收敛至 0.09，
        表明更强大的序列模型可以在该架构下进一步释放潜力。
      </p>
      <p style="margin-top:.8rem">
        <strong>架构展望：</strong>GameNN 的设计意义超越了单个模型本身。
        其侧枝架构（接口隔离 / 宿主无侵入 / 计算边界可控）使其可以作为"决策协处理器"
        嵌入任意系统——包括语言模型。MuLun-Mind 的 ThinkFuser 已验证了
        "LLM 直觉生成 + GameNN 理性校验"的双系统架构，这一范式可以直接用于缓解 LLM 幻觉问题：
        侧枝对 LLM 输出做事实核查，仅在置信度高时通过 Fuser 偏置修正 logits。
        结合世界模型的反事实推理能力（"如果我冲出去，80% 概率被狙"），
        GameNN 为 3A 游戏 NPC 的智能决策提供了高性价比的技术路径——
        训练成本集中在 GPU 集群，推理时仅需 CPU 单核 0.3ms。
      </p>
      <div class="keywords">
        <span class="kw">博弈决策架构</span>
        <span class="kw">分层强化学习</span>
        <span class="kw">世界模型</span>
        <span class="kw">侧枝架构</span>
        <span class="kw">RSSM</span>
        <span class="kw">MuLun 幕论</span>
        <span class="kw">Gumbel-Softmax</span>
        <span class="kw">Tank Chess</span>
        <span class="kw">LLM 幻觉抑制</span>
      </div>'''

data = data.replace(old_keywords, new_section)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(data)
print('Done: Chinese paper section updated')
